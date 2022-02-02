namespace WatReWeb.Models;

public class WaterReminder {
    bool isReminding = false;

    bool getIsReminder() { return isReminding; }
    void setReminder(bool isReminded) { this.isReminding = isReminded; }
}