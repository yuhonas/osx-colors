use framework "Foundation"
set theCenter to current application's NSDistributedNotificationCenter's defaultCenter()
theCenter's postNotificationName:"AppleColorPreferencesChangedNotification" object:(missing value) userInfo:(missing value) deliverImmediately:true
theCenter's postNotificationName:"AppleAquaColorVariantChanged" object:(missing value) userInfo:(missing value) deliverImmediately:true

