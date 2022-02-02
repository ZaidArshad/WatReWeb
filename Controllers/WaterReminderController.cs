using Microsoft.AspNetCore.Mvc;
using WatReWeb.Services;

namespace WatReWeb.Controllers;

[ApiController]
[Route("[controller]")]
public class WaterReminderController : ControllerBase {
    [HttpGet]
    public ActionResult<bool> Get() {
        return WaterReminderService.getRemindingStatus();
    }

    [HttpPut("{remind}")]
    public IActionResult RemindingStatus(bool remind) {
        if (remind != true && remind != false) return BadRequest();
        WaterReminderService.setRemindingStatus(remind);
        return NoContent();
    }
}