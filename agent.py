#!/usr/bin/env python
""" AI Agent.

AI Agents process data using local AI models.

MIT License

Copyright (c) 2021 Asociación de Investigacion en Inteligencia Artificial
Para la Leucemia Peter Moss

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

"""

import sys

from abc import ABC, abstractmethod

from modules.AbstractAgent import AbstractAgent

from modules.helpers import helpers
from modules.model import model


class agent(AbstractAgent):
	""" Acute Myeloid Leukemia Classifier 2021 AI Agent

	Represents a AI Agent that processes data
	using the Acute Myeloid Leukemia Classifier 2021 model.
	"""

	def train(self):
		""" Creates & trains the model. """

		self.model.prepare_data()
		self.model.prepare_network()
		self.model.train()
		self.model.evaluate()

	def set_model(self, mtype):

		self.model_type = mtype
		if self.model_type == "CNN":
			self.model = model(self.helpers)

	def load_model(self):
		""" Loads the trained model """

		self.model.load()

	def inference(self):
		""" Loads model and classifies test data locally """

		self.load_model()
		self.model.test()

	def signal_handler(self, signal, frame):
		self.helpers.logger.info("Disconnecting")
		sys.exit(1)


agent = agent()


def main():

	if len(sys.argv) < 2:
		print("You must provide an argument")
		exit()
	elif sys.argv[1] not in agent.helpers.confs["agent"]["params"]:
		print("Mode not supported! server, train or inference")
		exit()

	mode = sys.argv[1]

	if mode == "train":
		agent.set_model("CNN")
		agent.train()

	elif mode == "classify":
		agent.set_model("CNN")
		agent.inference()

if __name__ == "__main__":
	main()
