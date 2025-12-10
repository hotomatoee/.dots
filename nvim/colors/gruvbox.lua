local p = {
  bg0 = "#0f1010",
  bg1 = "#010101",
  bg2 = "#504945",
  bg3 = "#665c54",
  bg4 = "#7c6f64",

  fg0 = "#fafafa",
  fg1 = "#f6f6f6",
  fg2 = "#d5c4a1",
  fg3 = "#bdae93",
  fg4 = "#a89984",

  bright_red    = "#fb4934",
  bright_green  = "#b8bb26",
  bright_yellow = "#fabd2f",
  bright_blue   = "#83a598",
  bright_purple = "#d3869b",
  bright_aqua   = "#8ec07c",
  bright_gray   = "#928374",
  bright_orange = "#fe8019",

  dark_red    = "#cc241d",
  dark_green  = "#98971a",
  dark_yellow = "#d79921",
  dark_blue   = "#458588",
  dark_purple = "#b16286",
  dark_aqua   = "#689d6a",   -- you said this should be “green”
  dark_gray   = "#a89984",
  dark_orange = "#d65d0e",
}

local function hl(group, opts)
  vim.api.nvim_set_hl(0, group, opts)
end

vim.cmd("highlight clear")
vim.cmd("set background=dark")

-- Base UI
hl("Normal",        { fg = p.fg1, bg = p.bg0 })
hl("NormalFloat",   { fg = p.fg1, bg = p.bg1 })
hl("FloatBorder",   { fg = p.bg4, bg = p.bg1 })

hl("CursorLine",    { bg = p.bg1 })
hl("CursorColumn",  { bg = p.bg1 })
hl("Visual",        { bg = p.bg2 })

hl("LineNr",        { fg = p.bg4, bg = p.bg0 })
hl("CursorLineNr",  { fg = p.bright_yellow })

hl("StatusLine",    { fg = p.fg2, bg = p.bg1 })
hl("StatusLineNC",  { fg = p.bg4, bg = p.bg1 })
hl("VertSplit",     { fg = p.bg4 })

hl("Pmenu",         { fg = p.fg2, bg = p.bg1 })
hl("PmenuSel",      { fg = p.bg0, bg = p.bright_blue })

-- Syntax
hl("Comment",       { fg = p.bright_gray, italic = true })
hl("String",        { fg = p.dark_aqua })       -- your requested “green”
hl("Function",      { fg = p.bright_blue })
hl("Keyword",       { fg = p.dark_red })
hl("Identifier",    { fg = p.fg1 })
hl("Type",          { fg = p.dark_yellow })
hl("Number",        { fg = p.bright_orange })
hl("Boolean",       { fg = p.bright_orange })
hl("Constant",      { fg = p.bright_purple })
hl("Operator",      { fg = p.fg1 })
hl("Statement",     { fg = p.dark_red })

-- Treesitter (basic mappings)
hl("@comment",      { link = "Comment" })
hl("@string",       { link = "String" })
hl("@keyword",      { link = "Keyword" })
hl("@function",     { link = "Function" })
hl("@type",         { link = "Type" })
hl("@number",       { link = "Number" })
hl("@boolean",      { link = "Boolean" })

-- Diagnostics
hl("DiagnosticError", { fg = p.bright_red })
hl("DiagnosticWarn",  { fg = p.bright_yellow })
hl("DiagnosticInfo",  { fg = p.bright_blue })
hl("DiagnosticHint",  { fg = p.bright_aqua })

-- Misc
hl("Search",        { bg = p.bright_yellow, fg = p.bg0 })
hl("IncSearch",     { bg = p.bright_orange, fg = p.bg0 })

