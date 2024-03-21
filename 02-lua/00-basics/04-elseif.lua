local menu_option = 3
local menu_text

-- Comparison Operators
-- ~= NOT EQUAL
-- ==
-- >
-- <
-- >=
-- <=

if menu_option == 1 then
    menu_text = "Can I play, Daddy?"
elseif menu_option == 2 then
    menu_text = "Don't hurt me."
elseif menu_option == 3 then
    menu_text = "Bring 'em on!"
elseif menu_option == 4 then
    menu_text = "I am Death incarnate!"
end

print("Menu Option: " .. menu_text)