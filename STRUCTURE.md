# Structure
The basic structure is simple in DBF. You can look at DBF's structure like the HTML structure.

### Project Name
Within the first line of the file you set the project name / server name of the blueprint.
You do that with:
```
$$ 'project name'
```

### Roles
Next on the blueprint are the roles.
Within the roles you can set the simple herachie and order of the roles.
```
ROLES = {
    /'rolename' [ { permissions, color } ]
}
```

### Server
Within the Server section are all details about the categories and chanals of the server.
```
SERVER = {
    # categorie
        - text chat [ All ]
}
```

### Categories
A categorie can be created with a hashtag.
You can use categories to order your discord server.
```
    # test categories [ roles ]
```

