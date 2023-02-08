BUILD=${CURDIR}/build.sql
SCRIPTS=${CURDIR}/scripts
CSV='${CURDIR}/master_plan.csv'
ENV_LOCAL='${CURDIR}/.pgenv.local'
ENV_REMOTE='${CURDIR}/.pgenv.remote'
REMOTE_CSV='/usr/local/share/CM_Data/master_plan.csv'
MAIN=${CURDIR}/import.sql
NORMALIZE = ${CURDIR}/normalize.sql 
REMOTE_IMPORT = ${CURDIR}/import2.sql
SHELL := /usr/bin/env bash

all:
	@echo "Error: Please specify remote or local target!"

remote: clean main
	@cat $(IMPORT) >> $(BUILD)
	@cat $(NORMALIZE) >> $(BUILD)
	source $(ENV_REMOTE) && psql -h $${PGHOST} -d $${PGDATABASE} -U $${PGUSER} -f $(BUILD)

local: clean main
	@cat $(IMPORT) >> $(BUILD)
	@cat $(NORMALIZE) >> $(BUILD)
	source $(ENV_LOCAL) && psql -h $${PGHOST} -d $${PGDATABASE} -U $${PGUSER} -f $(BUILD)

main:
	@cat $(MAIN) >> $(BUILD)

import: main
	@echo "COPY import.master_plan FROM $(CSV_LOCAL) WITH DELIMITER ',' HEADER CSV;" >> $(BUILD)

normalize: import
	@cat $(NORMALIZE) >> $(BUILD)

clean:
	@rm -rf $(BUILD)
