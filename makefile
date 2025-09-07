ALEMBIC_CMD = alembic --raiseerr

.PHONY: help revision upgrade downgrade current history

help:
	@echo "Available commands:"
	@echo "  make revision name=your_message     Create new migration with a message"
	@echo "  make upgrade                        Apply latest migration"
	@echo "  make downgrade rev=base             Downgrade to revision (e.g., base, -1)"
	@echo "  make current                        Show current DB revision"
	@echo "  make history                        Show revision history"

revision:
	@if [ -z "$(name)" ]; then \
		$(ALEMBIC_CMD) revision --autogenerate; \
	else \
		$(ALEMBIC_CMD) revision --autogenerate -m "$(name)"; \
	fi


upgrade:
	$(ALEMBIC_CMD) upgrade head

downgrade:
	@if [ -z "$(rev)" ]; then \
		echo "Please provide a revision to downgrade to, e.g., make downgrade rev=base"; \
		exit 1; \
	fi
	$(ALEMBIC_CMD) downgrade $(rev)

current:
	$(ALEMBIC_CMD) current

history:
	$(ALEMBIC_CMD) history --verbose
