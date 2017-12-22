# ----------------------------------------------------------------------------
# Copyright (c) 2017-, labman development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .sample_plating_process import (
    SamplePlatingProcessListHandler, SamplePlatingProcessHandler)
from .gdna_extraction_process import GDNAExtractionProcessHandler

__all__ = ['SamplePlatingProcessListHandler', 'SamplePlatingProcessHandler',
           'GDNAExtractionProcessHandler']

PROCESS_ENDPOINTS = [
    (r"/process/sample_plating/([0-9]+)$", SamplePlatingProcessHandler),
    (r"/process/sample_plating$", SamplePlatingProcessListHandler),
    (r"/process/gdna_extraction$", GDNAExtractionProcessHandler)
]