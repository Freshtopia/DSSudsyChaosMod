import random
from lib2to3.pytree import Base

import psutil
from pymem import Pymem, process
from pymem.exception import ProcessNotFound

from .DarkSoulsRemastered.Effects import BaseEffect, WarpToBonfire
from .utils.ProcessTitles import ProcessTitles


class NoProcessFoundError(Exception):
    pass


class Effects:
    WarpToBonfire: WarpToBonfire


class ChaosHandler:
    def __init_(self):
        pass

    def get_options(self):
        effect_options = [
            BaseEffect,
            BaseEffect,
            WarpToBonfire,
        ]
        self.sampled_options = random.sample(effect_options, k=3)
        return self.sampled_options

    def hook(self):
        self.__find_process()

        if self.process_title is None:
            raise NoProcessFoundError

        try:
            pm = Pymem(self.process_title)
        except ProcessNotFound:
            raise NoProcessFoundError(f"Process {self.process_title} not found")

        self.pm = pm
        self.module = process.module_from_name(
            self.pm.process_handle, self.process_title
        )

    async def trigger_effect(self, effect=BaseEffect, seconds=60):
        self.current_effect = effect
        effect.start(self.pm, self.module)
        self.current_effect.stop(self.pm, self.module)

    def __find_process(self):
        self.process_title = None
        for process in psutil.process_iter():
            if process.name() == ProcessTitles.DSR:
                self.process_title = ProcessTitles.DSR
        return self.process_title
