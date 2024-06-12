import pytest
from . import request_response
from typing import Callable, Dict
from tests.fake_data import fake_data_obj
from pathlib import Path
import json
BASE_DIR: str = Path(__file__).resolve().parent



class TestAddition():

	@pytest.mark.parametrize(
		'params',
		[
			{
				'url': '/api/addition',
				'method': 'POST',
				'payload': fake_data_obj.get_list_sum_payload()
			}
		]
	)
	def test_sum_of_list_of_intergers(
		self: object,
		request_response: Callable
	):
		'''
			This function is used for create project.
		'''
		assert request_response.status_code == 200, "status code should be 200"
