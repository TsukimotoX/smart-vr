#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

static constexpr char TAG[] = "SmartVR";

extern "C" void app_main(void)
{
    ESP_LOGI(TAG, "SmartVR Receiver started!");

    while (true) {
        ESP_LOGI(TAG, "Receiver is alive");
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
