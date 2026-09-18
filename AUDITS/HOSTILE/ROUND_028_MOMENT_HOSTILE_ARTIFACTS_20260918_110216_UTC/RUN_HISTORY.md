# Execution and recording history

EXECUTION_HISTORY.json contains every acquisition/verification command,
the complete captured stdout and return metadata, authored patch contents,
the initial-command retrospective record, and the one orchestration error.
DISPLAY_HISTORY.json records the bounded re-emissions from captured output.
The very first cat output was not stored as a machine-captured session
variable; its exact source bytes are retained in INPUTS and INPUT_MANIFEST.
That initial record is explicitly marked retrospective, not fabricated
as an automatic transcript.

The command-history recorder necessarily stops before serializing itself.
Its final record explicitly identifies metadata serialization and the
pending fixed issuance command. The complete issuance source is
seal_packet.py; the terminal sibling VERIFY.log stores the actually
executed read-only verifier command, stdout, stderr and exit status after
all packet bytes were frozen. VERIFY.sha256 binds that receipt and seal.
This avoids a circular requirement to hash a manifest containing its own
future execution output.

The baseline program source digest, actual Python version, every complete
mutation stdout/stderr and every exit code are in CHECK_RESULTS.json and
CHECK_RUNS. No random sampling or dependency installation is involved.

The final issuance procedure rechecks all original twenty frozen source
files and copied inputs, copies the final standalone report into REPORT.md,
builds exact inventories/hashes, freezes regular files to 0444 and packet
directories to 0555, creates the archive and sibling seals, and invokes
the read-only portable verifier. It writes only named evidence outputs.
The issued report and artifact become immutable at that point.

