# bookcase

All the books at my house.

## Development

This is a [Django][https://www.djangoproject.com/] project set up with
[uv](https://github.com/astral-sh/uv).

Run development server:

```sh
uv run manage.py runserver
```

## Tools

[Ruff](https://github.com/astral-sh/ruff):

```sh
uv run ruff format
```

```sh
uv run ruff check --fix
```

[Djade](https://github.com/adamchainz/djade):

```sh
uv run djade main/templates/**/*.html
```

## License

Copyright sirodoht

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, version 3.
