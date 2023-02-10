@echo off
reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /v NullSessionPipes /t REG_MULTI_SZ /d \\.\pipe\test_pipe /f

reg add "HKLM\SYSTEM\CurrentControlSet\Control\LSA" /v restrictanonymous /t REG_DWORD /d 0 /f

if %ERRORLEVEL% == 0 (
  echo Successfully set RestrictAnonymous to 0
) else (
  echo Failed to set RestrictAnonymous to 0
)

pause
