namespace WatReWeb.Services;

public static class WaterReminderService {
    static bool isReminding = false;

    public static bool getRemindingStatus() { return isReminding; }
    public static void setRemindingStatus(bool status) { isReminding = status; }
}