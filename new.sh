mkdir $(date +%F) && \
    echo "### $(date +%F)" > $(date +%F)/index.md && \
    vim $(date +%F)/index.md
