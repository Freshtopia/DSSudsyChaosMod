from ChaosHandler.DarkSoulsRemastered.Memory import BaseAddress, PointerAddress
from ChaosHandler.Effect import BaseEffect
from pymem import memory


class Blind(BaseEffect):
    name = "Blinded"
    config_alias = "blind"

    async def onStart(self, pm, module):
        BaseCAR = BaseAddress.BaseCAR(pm, module)
        DrawDistancePointer = PointerAddress.DrawDistance(pm, BaseCAR)

        memory.write_float(pm.process_handle, DrawDistancePointer, 1)
        await self.tick(self.seconds, pm, module)

    async def onStop(self, pm, module):
        BaseCAR = BaseAddress.BaseCAR(pm, module)
        DrawDistancePointer = PointerAddress.DrawDistance(pm, BaseCAR)

        memory.write_float(pm.process_handle, DrawDistancePointer, 3100)
