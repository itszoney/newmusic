HEROKU = False   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = environ["SUDO_CHAT_ID"]
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 28053542
    API_HASH = "37f3f41000071041735523fab66d2355"
    SUDO_CHAT_ID = "-1001687657146"
    SESSION_STRING = "AQGsECYAuBJAuV7t42GcdYiyyN-dtsFi2eBrGAsGuZRRy7l7PgRZEXnB4TczMnMKDWMI9jeh8-C4mHW6R1Pke0N9WRqukyEzmOn2zlVx42oK6YrDsy3x0h6E5XXqxDUvUkIcwJNElY8_fwWCo1C7cLhVAVCfK2Cmfnh_4j0C-cm88ki8Mw7FCtJmiyvJq74W1iIxVBp7kv3jNTf2ELVJ8LMsSZkBHSn4qZr8xOWgdqS63a0kNmrfkx5-50CThbLalfYBrzBUFKG01LGYHUV1XBvHZ5D3F5qrtMoklac3cpO858Hk92raPwNYC3uKR8RGeGElWVAwdgKI5D0t59rSqiL6IFekCQAAAAE5hIeQAA"

# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
