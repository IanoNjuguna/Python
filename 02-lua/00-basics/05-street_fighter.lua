---------------------------------------------
-- Exercise:
--------------------------------------------
-- Display the correct name of the
-- attack "move" based on the name of
-- the game character.
--------------------------------------------
-- Name: Ryu -> Hadouken
-- Name: Chun Li -> Lightning Kick
-- Name: Guile -> Sonic Boom
-- Name: Honda -> Hundred Hand Slap
-- Name: Ken -> Hadouken
-- Name: Blanka -> Electric Shock
--------------------------------------------

local fighter_name = "kEN"
local attack_move
--------------------------------------------
-- TODO: select the correct attack move
--------------------------------------------
if string.lower(fighter_name) == "ryu"
or string.lower(fighter_name) == "ken" then
    attack_move = "Hadouken"
elseif string.lower(fighter_name) == "chun li" then
    attack_move = "Lightning Kick"
elseif string.lower(fighter_name) == "guile" then
	attack_move = "Sonic Boom"
elseif string.lower(fighter_name) == "honda" then
    attack_move = "Hundred Hand Slap"
elseif string.lower(fighter_name) == "blanka" then
	attack_move = "Electric Shock"
end


print(fighter_name .. " attacks with " .. attack_move)

