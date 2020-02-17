# The following lines were added by compinstall

zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate
zstyle :compinstall filename '/home/andrew/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt appendhistory notify
unsetopt autocd beep
bindkey -v
# End of lines configured by zsh-newuser-install

# ls uses colours by default
alias ls='ls --color=auto'

# Set the default text editor
export EDITOR=nvim

# dotfile configuration
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'

# Prompt
PROMPT='%F{yellow}%n@%m%f %F{blue}%~%f %(0?..%F{red}%B%?%b%f )%(1j.%F{green}%B[%j]%b%f.)
%F{yellow}%B%#%b%f '

# Source custom shell scripts from ~/bin
source /home/andrew/bin/dotfzf.sh
