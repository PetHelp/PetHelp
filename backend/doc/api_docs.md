# API endpoints

Die regulären Endpunkte können nur authentifiziert genutzt weden.
Das Token muss im  Authorization-Header mit dem Prefix "Bearer " gesendet werden.

## Register user
- endpoint: /register/
- payload: {name: "name", email: "email@test.de", password: "secret"}

## Reset password
- endpoint: /reset-password
- payload: {email: "email@test.de"}

## Login/Get Token
- endpoint: /token
- payload: {email: "email@test.de", password: "secret}
- response: {access: access_token, refresh: refresh_token}

## Animals
- endpoint: /animals/
- payload {}

## HelpRequests
- endpoint: /help-requests/
- payload {}

## HelpOffers
- endpoint: /help-offers/
- payload {}
