#!/usr/bin/env python
""" Abstract class representing a AI Agent.

Represents a AI Agent. AI Agents process data using local AI
models.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors:
- Adam Milton-Barker

"""

import psutil
import requests
import threading

from abc import ABC, abstractmethod

from modules.helpers import helpers
from modules.model import model

from threading import Thread


class AbstractAgent(ABC):
	""" Abstract class representing a AI Agent.

	This object represents a AI Agent. AI Agents
	process data using local AI models.

	Attributes
	----------
	NA

	Methods
	-------
	mqtt_conn()
		Creates a MQTT connection with the iotJumpWay
		private MQTT broker.
	"""

	def __init__(self):
		"Initializes the abstract_agent object."
		super().__init__()

		self.helpers = helpers("Agent")
		self.confs = self.helpers.confs
		self.credentials = self.helpers.credentials
		self.model_type = None

		self.helpers.logger.info("Agent initialization complete.")

	@abstractmethod
	def set_model(self):
		""" Creates & trains the model. """
		pass

	@abstractmethod
	def train(self):
		""" Creates & trains the model. """
		pass

	@abstractmethod
	def load_model(self):
		""" Loads model and classifies test data locally """
		pass

	@abstractmethod
	def inference(self):
		""" Loads model and classifies test data """
		pass
