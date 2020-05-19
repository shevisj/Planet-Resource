FROM python:3.8.2 AS build

WORKDIR /usr/src/app/

COPY . .

RUN set -eux; \
    pip install ./game

###

FROM build AS dev

ENTRYPOINT ["/bin/bash"]

###

FROM build AS test

RUN set -eux; \
    pip install './game[test]'

CMD ["python", "-m", "pytest", "--verbose", "./game/tests/"]

###

FROM build AS sim

ARG SIM_FILE=*

CMD ["python", "./simulations/run_sims.py", "*"]
