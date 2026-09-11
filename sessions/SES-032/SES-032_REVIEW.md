# SES-032 — poprawka i test następnego styku

**Status:** AUDIT FINDING

## Ustalenie

SES-032 potwierdził rzeczywiste przejście:

`Intent Envelope → VALID Specification → BuildPlan`

Najbliższy rzeczywisty styk wymagający domknięcia to:

`Specification → PROPOSED element → READY_FOR_APPROVAL → explicit Human Approval → AUTHORIZED`

SES-008 obecnie buduje wymagania jako `DERIVED` i nie tworzy `PROPOSED` elementów. SES-010 i SES-014 definiują jednak `PROPOSED` jako prawidłowy przypadek wymagający jawnej decyzji człowieka.

## Zasada poprawkowa

Nie wolno dodawać sztucznego `PROPOSED` wyłącznie w teście. Najpierw należy ustalić, czy istnieje w obecnym modelu naturalny sygnał wejściowy oznaczający brak jednoznacznego wyboru. Jeśli istnieje — należy go zachować przez SES-008. Jeśli nie istnieje — nie należy wymyślać nowego mechanizmu bez osobnego uzasadnienia.

## Następny test

Zbudować test integracyjny obejmujący istniejące kontrakty i sprawdzający, że:

1. `VALID Specification` tworzy `BuildPlan`;
2. element rzeczywiście oznaczony `PROPOSED` pozostaje `PROPOSED`;
3. plan przechodzi do `READY_FOR_APPROVAL`;
4. brak jawnej zgody zatrzymuje przejście;
5. jawna zgoda związana z właściwym `build_plan_id` tworzy `EXECUTION_AUTHORIZATION`;
6. autoryzacja nie oznacza jeszcze wykonania.

Nie uznawać testu za dowód, jeżeli wymaga ręcznego ustawiania statusu planu lub omijania kontraktu.
