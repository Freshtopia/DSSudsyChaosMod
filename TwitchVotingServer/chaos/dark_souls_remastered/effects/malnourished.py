from chaos.dark_souls_remastered.dsr_effect import DSREffect
from chaos.dark_souls_remastered.memory import BaseAddress, Pointer
from pymem import memory


class Malnourished(DSREffect):
    name = "Malnourished"
    config_alias = "malnourished"

    async def _set_arm_size(self, size):
        BaseB = BaseAddress.BaseB(self.pm, self.module)
        arm_pointer = Pointer.Player.Body.arm_size(self.pm, BaseB)
        memory.write_float(self.pm.process_handle, arm_pointer, size)

    async def _set_head_size(self, size):
        BaseB = BaseAddress.BaseB(self.pm, self.module)
        head_pointer = Pointer.Player.Body.head_size(self.pm, BaseB)
        memory.write_float(self.pm.process_handle, head_pointer, size)

    async def _set_chest_size(self, size):
        BaseB = BaseAddress.BaseB(self.pm, self.module)
        chest_pointer = Pointer.Player.Body.chest_size(self.pm, BaseB)
        memory.write_float(self.pm.process_handle, chest_pointer, size)

    async def _set_leg_size(self, size):
        BaseB = BaseAddress.BaseB(self.pm, self.module)
        leg_pointer = Pointer.Player.Body.leg_size(self.pm, BaseB)
        memory.write_float(self.pm.process_handle, leg_pointer, size)

    async def _set_ab_size(self, size):
        BaseB = BaseAddress.BaseB(self.pm, self.module)
        ab_pointer = Pointer.Player.Body.ab_size(self.pm, BaseB)
        memory.write_float(self.pm.process_handle, ab_pointer, size)



    async def _on_start(self):
        await self._set_arm_size(-3)
        await self._set_head_size(-2)
        await self._set_chest_size(-5)
        await self._set_leg_size(-3)
        await self._set_ab_size(-3)
        await self.tick(self.seconds)

    async def _on_stop(self):
        await self._set_arm_size(0)
        await self._set_head_size(0)
        await self._set_chest_size(0)
        await self._set_leg_size(0)
        await self._set_ab_size(0)