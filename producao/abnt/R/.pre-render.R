# Pre-render Script - Simplified for SEINUC/IDEFLOR
#
# Este script foi simplificado para remover dependências não-essenciais.
# O template funcionará sem as funcionalidades avançadas do template original.

# Load Basic Packages -----
library(fs)
library(here)

# Copy Images Folder to `qmd` -----
# Resolve issues with relative paths.

dir_path <- here("qmd", "images")

if (!dir.exists(dir_path)) {
  dir.create(dir_path) |> invisible()
}

# Copy images if they exist
if (dir.exists(here("images"))) {
  for (i in dir_ls(here("images"), type = "file")) {
    file_copy(
      path = i,
      new_path = file.path(dir_path, basename(i)),
      overwrite = TRUE
    )
  }
}

# NOTE: Advanced TeX file updates from the original template have been disabled.
# If you need to use advanced pre-textual elements (approval sheets, errata, etc.),
# you may need to reinstall the 'quartor' package from GitHub:
# remotes::install_github("danielvartan/quartor")
#
# Or edit those elements directly in the tex/ files.

cat("Pre-render completed successfully (simplified mode)\n")
