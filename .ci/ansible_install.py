#!/usr/bin/env python

import ci_lib

batches = [
    [
        'if [ "${TF_BUILD:-false}" = "True" ]; then aws ecr-public get-login-password | docker login --username AWS --password-stdin public.ecr.aws; fi',
    ]
]

ci_lib.run_batches(batches)
