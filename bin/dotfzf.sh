# Creates a fzf finder where the items to find are the filenames
# in the dotfiles bare git repo. After selection, the filename will
# be prepended with the dotfiles repo root directory.
function dotfzf {
	ROOT=$(dotfiles rev-parse --show-toplevel)
	dotfiles ls-files --full-name :/ | fzf | awk -vROOT="$ROOT/" '{print ROOT $0}'
}
