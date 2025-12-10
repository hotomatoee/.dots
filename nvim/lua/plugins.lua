local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"

if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end

vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  {
    "saghen/blink.cmp",
    dependencies = {
      "rafamadriz/friendly-snippets",
    },
    version = "*",

    opts = {
      keymap = {
        preset = "super-tab",
        ["<UP>"] = { "select_prev", "fallback" },
        ["<DOWN>"] = { "select_next", "fallback" },
        ["<LEFT>"] = { "scroll_documentation_up", "fallback" },
        ["<RIGHT>"] = { "scroll_documentation_down", "fallback" },
        ["<C-k>"] = { "show_signature", "hide_signature", "fallback" },
      },

      appearance = {
        nerd_font_variant = "mono",
      },

      sources = {
        default = { "lsp", "path", "snippets", "buffer" },
      },

      fuzzy = {
        implementation = "prefer_rust_with_warning",
      },

      completion = {
        keyword = { range = "prefix" },
        menu = {
          draw = {
            treesitter = { "lsp" },
          },
        },
        trigger = { show_on_trigger_character = true },
        documentation = {
          auto_show = true,
        },
      },

      signature = { enabled = true },
    },

    opts_extend = { "sources.default" },
  },

  {
    "mason-org/mason.nvim",
    opts = {},
  },

  {
    "nvimdev/dashboard-nvim",
    lazy = false,

    opts = function()
      local logo = [[
         ██╗      █████╗ ███████╗██╗   ██╗██╗   ██╗██╗███╗   ███╗
         ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██║   ██║██║████╗ ████║
         ██║     ███████║  ███╔╝  ╚████╔╝ ██║   ██║██║██╔████╔██║
         ██║     ██╔══██║ ███╔╝    ╚██╔╝  ╚██╗ ██╔╝██║██║╚██╔╝██║
         ███████╗██║  ██║███████╗   ██║    ╚████╔╝ ██║██║ ╚═╝ ██║
         ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝     ╚═══╝  ╚═╝╚═╝     ╚═╝
      ]]

      logo = string.rep("\n", 8) .. logo .. "\n\n"

      local opts = {
        theme = "doom",

        hide = {
          statusline = false,
        },

        config = {
          header = vim.split(logo, "\n"),

          center = {
            {
              action = 'lua LazyVim.pick()()',
              desc = " Find File",
              icon = " ",
              key = "f",
            },
            {
              action = "ene | startinsert",
              desc = " New File",
              icon = " ",
              key = "n",
            },
            {
              action = 'lua LazyVim.pick("oldfiles")()',
              desc = " Recent Files",
              icon = " ",
              key = "r",
            },
            {
              action = 'lua LazyVim.pick("live_grep")()',
              desc = " Find Text",
              icon = " ",
              key = "g",
            },
            {
              action = 'lua LazyVim.pick.config_files()()',
              desc = " Config",
              icon = " ",
              key = "c",
            },
            {
              action = 'lua require("persistence").load()',
              desc = " Restore Session",
              icon = " ",
              key = "s",
            },
            {
              action = "LazyExtras",
              desc = " Lazy Extras",
              icon = " ",
              key = "x",
            },
            {
              action = "Lazy",
              desc = " Lazy",
              icon = "󰒲 ",
              key = "l",
            },
            {
              action = function()
                vim.api.nvim_input("<cmd>qa<cr>")
              end,
              desc = " Quit",
              icon = " ",
              key = "q",
            },
          },

          footer = function()
            local stats = require("lazy").stats()
            local ms = (math.floor(stats.startuptime * 100 + 0.5) / 100)
            return {
              "⚡ Neovim loaded "
                .. stats.loaded
                .. "/"
                .. stats.count
                .. " plugins in "
                .. ms
                .. "ms",
            }
          end,
        },
      }

      for _, button in ipairs(opts.config.center) do
        button.desc = button.desc .. string.rep(" ", 43 - #button.desc)
        button.key_format = "  %s"
      end

      if vim.o.filetype == "lazy" then
        vim.api.nvim_create_autocmd("WinClosed", {
          pattern = tostring(vim.api.nvim_get_current_win()),
          once = true,
          callback = function()
            vim.schedule(function()
              vim.api.nvim_exec_autocmds("UIEnter", { group = "dashboard" })
            end)
          end,
        })
      end

      return opts
    end,
  },
})




