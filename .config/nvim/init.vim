"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=/home/andrew/.cache/dein/repos/github.com/Shougo/dein.vim

" Required:
if dein#load_state('/home/andrew/.cache/dein')
  call dein#begin('/home/andrew/.cache/dein')

  " Let dein manage dein
  " Required:
  call dein#add('/home/andrew/.cache/dein/repos/github.com/Shougo/dein.vim')

  " Gruvbox colour scheme
  call dein#add('morhetz/gruvbox')

  " Lightline
  call dein#add('itchyny/lightline.vim')

  " vim-tmux-navigator
  call dein#add('christoomey/vim-tmux-navigator')

  " fugitive (git wrapper)
  call dein#add('tpope/vim-fugitive')

  " fzf
  call dein#add('junegunn/fzf')
  call dein#add('junegunn/fzf.vim')

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" Install uninstalled dein plugins on startup
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------

" Remap leader key to ,
let mapleader = ","

" Relative line-numbering (with current line number on cursor line)
set number relativenumber

" Highlight current line
set cursorline

" 80 column highlight
set textwidth=80
set colorcolumn=+1

"--------------------------------------
" Navigation settings
"--------------------------------------

" Switch to previous buffer
nnoremap <leader>bb :bp<CR>

" FZF File search
nnoremap <leader>f :Files<CR>

"--------------------------------------
" Plugin-specific settings
"--------------------------------------

" itchyny/lightline
set noshowmode " to hide the "-- INSERT --" string

" morhetz/gruvbox
let g:gruvbox_contrast_dark='soft'
let g:gruvbox_italic=1
colorscheme gruvbox

" tpope/vim-fugitive
nnoremap <leader>gs :Gstatus<CR>
nnoremap <leader>gw :Gwrite<CR>
nnoremap <leader>gc :Gcommit<CR>
