BUILD=${CURDIR}/build.sql
SCRIPTS=${CURDIR}/scripts
CSV='${CURDIR}/master_plan.csv'
REMOTE_CSV='/usr/local/share/CM_Data/master_plan.csv'
MAIN=$(SCRIPTS)/import.sql
NORMALIZE = $(SCRIPTS)/normalize.sql 
REMOTE_IMPORT = $(SCRIPTS)/remote_import.sql

all: normalize
	psql $(DB) -f $(BUILD)

remote: clean main
	@cat $(REMOTE_IMPORT) >> $(BUILD)
	@cat $(NORMALIZE) >> $(BUILD)
	psql -h $(DBSERV) -d $(DB) -U $(PGUSER) -f $(BUILD)
	
main:
	@cat $(MAIN) >> $(BUILD)

import: main
	@echo "COPY import.master_plan FROM $(CSV) WITH DELIMITER ',' HEADER CSV;" >> $(BUILD)

normalize: import
	@cat $(NORMALIZE) >> $(BUILD)

clean:
	@rm -rf $(BUILD)
