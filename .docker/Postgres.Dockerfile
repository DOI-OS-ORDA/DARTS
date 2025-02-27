FROM postgres:15.7

COPY ./.docker/acronyms.ths /usr/share/postgresql/15/tsearch_data/
