# API endpoints

Die regulären Endpunkte können nur authentifiziert genutzt weden.
Das Token muss im  Authorization-Header mit dem Prefix "Bearer " gesendet werden.

## User

* [Register](register/post.md): `POST /register/`
* [Reset password](reset-password/post.md): `POST /reset-password/`
* [Login](token/post.md): `POST /token/`

## Animals

### GET /animals/

Liefert Liste von Tier-Ids?
Liefert Liste von Tieren?
Liefert nur ein Tier?

payload:

```
{
}
```

response:

```
```


### POST /animals/

Speichert ein neues Tier.
Aktualisiert auch ein bestehendes Tier oder separater Endpunkt gewünscht?

payload:
 
```
  {
    name: "Gamma",
    type: 1,
    image: ?,
    location: ?,
    description: "Ein ganz Lieber!",
    tags: [1, 2, 3]
  }
```

## HelpRequests

### GET /featured-help-requests/

Gibt die Liste der Hilfsgesuche für die Startseite.
Dieser Endpoint kann auch nicht authentifiziert genutzt werden.

payload: {}

response:

```
[
  {
    name: "Gamma",
    location: "Hamburg",
    emergency: true
  },
  ...
]
```

### GET /help-requests/

Liefert (gefilterte) Hilfsgesuche?

payload:

```
{
  filter?
}
```

response:
```
[
  {
    ...
  },
  ...
]
```


## HelpOffers

### GET /featured-help-offers/

Liefert die Hilfsangebote für die Startseite.
Dieser Endpoint kann auch nicht authentifiziert genutzt werden.

payload: {}

response:

```
[
  {
    id: 1,
    name: "Kathi König",
    location: "Hamburg",
    teaser: "Hier steht etwas über sie\nHier steht noch mehr über sie"
  }
]
```

### GET /help-offers/

payload:

```
{
  filter?
}
```

response:
```
[
  {
    ...
  },
  ...
]
```

### POST /help-offers/

Erstellt ein neues (sofort aktives?) Hilfsangebot.
Aktualisiert es auch ein bestehendes Hilfsangebot oder separater Endpunkt gewünscht?

payload:

```
{
  help_type: 1,
  animal_type: 1,
  description: "Biete Spaziergänge",
  activate?
}
```
