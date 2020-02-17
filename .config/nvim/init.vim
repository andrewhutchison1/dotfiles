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

" Lightline settings
set noshowmode " to hide the "-- INSERT --" string

" morhetz/gruvbox settings
let g:gruvbox_contrast_dark='soft'
let g:gruvbox_italic=1
colorscheme gruvbox

