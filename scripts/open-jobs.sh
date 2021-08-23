#!/bin/bash
set -euo pipefail

SITES=(
    "https://angel.co/jobs"
    "https://weworkremotely.com/remote-jobs/search?term=&button=&categories%5B%5D=18&region%5B%5D=Anywhere+%28100%25+Remote%29+Only&region%5B%5D=Asia+Only"
    "https://www.python.org/jobs/"
    "https://www.workatastartup.com/companies?companySize=any&expo=any&industry=any&jobType=any&layout=list-compact&remote=any&role=matching&sortBy=created_desc"
    "https://stackoverflow.com/jobs?r=true&tl=python"
    "https://remoteok.io/remote-dev+python-jobs?location=worldwide"
    "https://djangojobs.net/jobs/?location=&remote=true"
)

firefox ${SITES[*]} --new-window &
