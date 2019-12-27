from django.contrib import admin
from guardian.admin import GuardedModelAdmin
import nested_admin

from .models import (Backup, BackupMethod, TargetDevice, Device, RamType, Ram,
                     DiskType, Owner, Disk, CpuArchitecture, CpuManufacturer,
                     Cpu, OperatingSystem, Computer, Raid,
                     ComputerDiskRelation, DisksInRaid, RaidType,
                     ComputerCpuRelation, ComputerSoftwareRelation,
                     ComputerRamRelation, Warranty, WarrantyType, Customer,
                     DeviceCategory, ConnectedDevice, DeviceInNet, Net,
                     DeviceManufacturer, AdGroup, MailGroup, Location,
                     MailAlias, IpStatus, Notification, NotificationType,
                     SoftwareArchitecture, SoftwareCategory, Software, User,
                     UserInAdGroup, UserInMailGroup)


class CustomerAdmin(GuardedModelAdmin):
    pass


class CpuAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class CpuArchitectureAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class BackupMethodAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class CpuManufacturerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DeviceCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DeviceManufacturerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class IpStatusAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class MailAliasAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class NotificationTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class NotificationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class OperatingSystemAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RamModuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RaidTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SoftwareArchitectureAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SoftwareCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class TargetDeviceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DiskTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RamTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserInAdGroupAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserInMailGroupAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class WarrantyTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DiskInRaidAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SoftwareInLine(nested_admin.NestedStackedInline):
    model = ComputerSoftwareRelation
    extra = 0
    verbose_name_plural = 'Software'


class RamInLine(nested_admin.NestedStackedInline):
    model = ComputerRamRelation
    extra = 0
    verbose_name_plural = 'RAM Modules'


class DiskInLine(nested_admin.NestedStackedInline):
    model = ComputerDiskRelation
    extra = 0
    verbose_name_plural = 'Disks'


class DisksInRaidInLine(nested_admin.NestedStackedInline):
    model = DisksInRaid
    extra = 0
    verbose_name_plural = 'Disks in RAID'


class CpusInLine(nested_admin.NestedStackedInline):
    model = ComputerCpuRelation
    extra = 0
    verbose_name_plural = 'CPUs'


class RaidInLine(nested_admin.NestedStackedInline):
    model = Raid
    extra = 0
    verbose_name_plural = 'RAID'
    inlines = (DisksInRaidInLine,)


class DeviceInNetInline(nested_admin.NestedStackedInline):
    model = DeviceInNet
    extra = 0
    verbose_name_plural = 'Nets'


class ComputerAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'host')
    inlines = (SoftwareInLine, CpusInLine, RamInLine, DiskInLine, RaidInLine,
               DeviceInNetInline)


class AdGroupInLine(admin.StackedInline):
    model = UserInAdGroup
    extra = 0
    verbose_name_plural = 'AD Groups'


class MailGroupInLine(admin.StackedInline):
    model = UserInMailGroup
    extra = 0
    verbose_name_plural = 'Mail Groups'


class MailAliasInLine(admin.StackedInline):
    model = MailAlias
    extra = 0
    verbose_name_plural = 'Mail Aliases'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'enabled')
    inlines = (AdGroupInLine, MailGroupInLine, MailAliasInLine)


class TargetDeviceInLine(admin.StackedInline):
    model = TargetDevice
    extra = 0
    verbose_name_plural = 'Target Devices'


class BackupAdmin(admin.ModelAdmin):
    inlines = (TargetDeviceInLine,)


admin.site.register(AdGroup)
admin.site.register(Backup, BackupAdmin)
admin.site.register(BackupMethod, BackupMethodAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(ConnectedDevice)
admin.site.register(Cpu, CpuAdmin)
admin.site.register(CpuArchitecture, CpuArchitectureAdmin)
admin.site.register(CpuManufacturer, CpuManufacturerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Device)
admin.site.register(DeviceCategory, DeviceCategoryAdmin)
admin.site.register(DeviceInNet)
admin.site.register(DeviceManufacturer, DeviceManufacturerAdmin)
admin.site.register(Disk)
admin.site.register(DiskType, DiskTypeAdmin)
admin.site.register(IpStatus, IpStatusAdmin)
admin.site.register(Location)
admin.site.register(MailAlias, MailAliasAdmin)
admin.site.register(MailGroup)
admin.site.register(Net)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationType, NotificationTypeAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(Owner)
admin.site.register(RaidType, RaidTypeAdmin)
admin.site.register(Ram, RamModuleAdmin)
admin.site.register(RamType, RamTypeAdmin)
admin.site.register(Software)
admin.site.register(SoftwareArchitecture, SoftwareArchitectureAdmin)
admin.site.register(SoftwareCategory, SoftwareCategoryAdmin)
admin.site.register(TargetDevice, TargetDeviceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserInAdGroup, UserInAdGroupAdmin)
admin.site.register(UserInMailGroup, UserInMailGroupAdmin)
admin.site.register(Warranty)
admin.site.register(WarrantyType, WarrantyTypeAdmin)

