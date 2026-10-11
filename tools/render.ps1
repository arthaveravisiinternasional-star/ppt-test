param(
    [string]$File,
    [string]$Mode = 'png',      # png | pdf | embed
    [string]$Dir,
    [string]$Slides = ''        # e.g. "3,7" (png mode only)
)
# Load Fredoka / Varela Round for this session (per-user fonts are not always loaded after a reboot)
Add-Type -Namespace ScanvasFonts -Name Gdi -MemberDefinition '[DllImport("gdi32.dll", CharSet = CharSet.Unicode)] public static extern int AddFontResource(string f);' -ErrorAction SilentlyContinue
$fontDir = Join-Path (Split-Path $PSScriptRoot -Parent) 'assets\fonts'
foreach ($f in 'Fredoka-Bold.ttf', 'Fredoka-SemiBold.ttf', 'VarelaRound-Regular.ttf', 'RobotoCondensed-Regular.ttf', 'RobotoCondensed-Bold.ttf', 'RobotoCondensed-SemiBold.ttf') {
    $path = Join-Path $fontDir $f
    if (Test-Path $path) { [void][ScanvasFonts.Gdi]::AddFontResource($path) }
}
$app = New-Object -ComObject PowerPoint.Application
$readOnly = $Mode -ne 'embed'
$p = $app.Presentations.Open($File, $readOnly, $false, $false)
if ($Mode -eq 'embed') {
    # re-save with TrueType fonts embedded (Fredoka / Varela Round travel with the file)
    $p.SaveAs($File, 24, -1)   # ppSaveAsOpenXMLPresentation, EmbedTrueTypeFonts = msoTrue
    Write-Output "fonts embedded -> $File"
} elseif ($Mode -eq 'pdf') {
    $pdf = [System.IO.Path]::ChangeExtension($File, '.pdf')
    $p.SaveAs($pdf, 32)   # ppSaveAsPDF
    Write-Output "pdf $pdf"
} else {
    New-Item -ItemType Directory -Force $Dir | Out-Null
    $want = @()
    if ($Slides) { $want = $Slides.Split(',') | ForEach-Object { [int]$_ } }
    foreach ($s in $p.Slides) {
        if ($want.Count -eq 0 -or $want -contains $s.SlideIndex) {
            $s.Export("$Dir\slide$($s.SlideIndex).png", 'PNG', 1600, 900)
        }
    }
    Write-Output "png -> $Dir"
}
$p.Close(); $app.Quit()
