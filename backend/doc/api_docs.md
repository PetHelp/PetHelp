# API endpoints

Die regulären Endpunkte können nur authentifiziert genutzt weden.
Das Token muss im  Authorization-Header mit dem Prefix "Bearer " gesendet werden.

## Login

* [Register](register/post.md): `POST /register/`
* [Reset password](reset-password/post.md): `POST /reset-password/`
* [Login](token/post.md): `POST /token/`

## Animals
- endpoint: /animals/
- payload {}

## HelpRequests
- endpoint: /help-requests/
- payload {}

## HelpOffers
- endpoint: /help-offers/
- payload {}
