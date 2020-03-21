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
- endpoint: /featured-animals/
- payload {}
- response: [{name: "Gamma", location: "Hamburg", emergency: true}, ...]

- endpoint: GET /animals/
- payload {filter?}
- response: [{name: "Gamma", location: "Hamburg", emergency: true, type: "Hund", image: "gamma.jpg", owner: {}, description: "Ein ganz Lieber!", tags: [1, 2, 3]}, ...]

- endpoint: POST /animals/
- payload {name: "Gamma", type: 1, image: ?, location: ?, description: "Ein ganz Lieber!", tags: [1, 2, 3]}


## HelpRequests
- endpoint: /help-requests/
- payload {}

## HelpOffers
- endpoint: /featured-help-offers/
- payload {}
- response: [{id: 1, name: "Kathi König", location: "Hamburg", teaser: "Hier steht etwas über sie\nHier steht noch mehr über sie"}]

- endpoint: GET /help-offers/
- payload {}
- response: [...]

- endpoint: POST /help-offers/
- payload {help_type: 1, animal_type: 1, description: "Biete Spaziergänge", activate?}
