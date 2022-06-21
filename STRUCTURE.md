# Structure
The basic structure is simple in DBF. You can look at DBF's structure like the HTML structure.


---
## Content
[Project Name](#project-name)\
[Roles](#roles)\
[Server](#server)\
[Categories](#categories)\
[Chanals](#chanals)\
[Permissions](#permissions)\
[Bots](#bots)


---
### Project Name
Within the first line of the file you set the project name / server name of the blueprint.
You do that with:
```
$$ 'project name'
```

---
### Roles
Next on the blueprint are the roles.
Within the roles you can set the simple herachie and order of the roles.
```
ROLES = {
    /'rolename' [ { permissions, color } ]
}
```

---
### Server
Within the Server section are all details about the categories and chanals of the server.
```
SERVER = {
    # categorie
        - text chat [ All ]
}
```

----
### Categories
A categorie can be created with a hashtag.
You can use categories to order your discord server.
```
    # test categories [ roles ]
```

---
### Chanals
A Chanal can be added everywhere inside the SERVER.
A chanals can ba a text chat or a voice chat.
The different types of chanal are marked by there prefix.
```
    - text chat
    + voice chat
    ~ announcement chanal
    R rules chanal
    W welcome chanal
    M meeting chanal
```

---
### Permissions
You can also plan the role permissions witin the blueprint. you can do that by adding the following after a chanal, category or role:
```
role [ permissions ]
```

---
### Bots
you can also add features of bots in the blueprint.
One thing thats needed for that is "initilising the bot" you do that by adding the following option to the SERVER Tag:
```
SERVER [ YourBot, YourBot2 ] = {

}
```

To plan the features you can add the following under the chanal or categorie:
``` 
- ticket test [ BOT: YourTicketBot, = ]{
    = Open Ticket
    = Ask Question
}
```