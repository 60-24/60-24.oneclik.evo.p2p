package org.p2p6024.android;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity {
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private TextView status;
    private EditText host;
    private EditText port;
    private EditText label;
    private EditText message;

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        int pad = 24;
        root.setPadding(pad, pad, pad, pad);

        TextView title = new TextView(this);
        title.setText("P2P 60-24 Android Node");
        title.setTextSize(22);
        root.addView(title);

        label = field("Node label", "A");
        host = field("Host", "192.168.1.20");
        port = field("Port", "39001");
        message = field("Message", "hello-from-Android");

        root.addView(label);
        root.addView(host);
        root.addView(port);
        root.addView(message);

        LinearLayout buttons = new LinearLayout(this);
        buttons.setOrientation(LinearLayout.HORIZONTAL);

        Button connect = new Button(this);
        connect.setText("Connect");
        connect.setOnClickListener(v -> run("connect"));

        Button listen = new Button(this);
        listen.setText("Listen once");
        listen.setOnClickListener(v -> run("listen"));

        buttons.addView(connect, new LinearLayout.LayoutParams(0, -2, 1));
        buttons.addView(listen, new LinearLayout.LayoutParams(0, -2, 1));
        root.addView(buttons);

        status = new TextView(this);
        status.setText("Ready. Use Connect for Linux Node B or Listen once for Android Node B.");
        status.setTextIsSelectable(true);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(status);
        root.addView(scroll, new LinearLayout.LayoutParams(-1, 0, 1));

        setContentView(root);
    }

    private EditText field(String hint, String value) {
        EditText field = new EditText(this);
        field.setHint(hint);
        field.setText(value);
        field.setSingleLine(true);
        return field;
    }

    private void run(String mode) {
        String h = host.getText().toString().trim();
        String p = port.getText().toString().trim();
        String l = label.getText().toString().trim();
        String m = message.getText().toString();

        status.setText("Running " + mode + "...");
        executor.submit(() -> {
            try {
                Python py = Python.getInstance();
                PyObject module = py.getModule("android_p2p");
                PyObject result;
                if ("connect".equals(mode)) {
                    result = module.callAttr("connect", h, Integer.parseInt(p), l, m);
                } else {
                    result = module.callAttr("listen", h, Integer.parseInt(p), l);
                }
                show(result.toString());
            } catch (Exception e) {
                show("ERROR " + e.getClass().getSimpleName() + ": " + e.getMessage());
            }
        });
    }

    private void show(String text) {
        runOnUiThread(() -> status.setText(text));
    }

    @Override
    protected void onDestroy() {
        executor.shutdownNow();
        super.onDestroy();
    }
}
