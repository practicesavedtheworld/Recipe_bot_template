# Recipe_bot_template
Template for recipe based tg bots. Integrate it with your food/recipe bot as a base


-------
## What is this?
The recipe based Telegram Bot Template, a bot that provides food recipes or ingredients for cooking to users.
This template can be integrated with your bot to handle queries and provide recipe information.
-------
## Require

-------

`make` tool

`Docker >= 25 `

`docker compose >= 2.24`

---
## Run as container

---
Make sure your env file contain correct hostname for connection to the database.
If you familiar with docker you can change host/port whenever you want

```
DATABASE_HOST=mongo
DATABASE_PORT=27017

DATABASE_HOST_TEST=mongo
DATABASE_PORT_TEST=27017
```

start command:
1) ```
   git clone https://github.com/practicesavedtheworld/Recipe_bot_template.git
   ```
2) ```
   cd Recipe_bot_template
   ```
3) ```
   docker compose up --build
   ```


---

## Run as python script

---

It requires python v3.12.
1) ```
   git clone https://github.com/practicesavedtheworld/Recipe_bot_template.git
   ```
2) ```
   cd Recipe_bot_template
   ```
3)

<b>Without poetry</b>

```
make run_as_script
```

<b>With poetry</b>

```
make run_as_script_poetry
```

<b>[Optional] Add default RU recipes</b>

<b>Without poetry</b>

```
make default_recipes
```

<b>With poetry</b>

```
make default_recipes_poetry
```

---

## Run tests

---

1) ```
   git clone https://github.com/practicesavedtheworld/Recipe_bot_template.git
   ```
2) ```
   cd Recipe_bot_template
   ```
3)

<b>Without poetry</b>

```
make tests
```

<b>With poetry</b>

```
make tests_poetry
```




