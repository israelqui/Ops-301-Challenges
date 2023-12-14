# Define user details
$firstName = "name "
$lastName = "last"
$displayName = "$firstName $lastName"
$office = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$company = "GlobeX USA"

# Create the user
New-ADUser -Name $displayName -GivenName $firstName -Surname $lastName -DisplayName $displayName -SamAccountName $firstName.ToLower() -EmailAddress $email -Office $office -Department $department -Company $company -AccountPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Enabled $true

# Check if the user was created
Get-ADUser -Filter "EmailAddress -eq '$email'"

