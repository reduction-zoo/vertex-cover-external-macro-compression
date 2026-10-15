import Challenge
open VertexCoverExternalMacroCompression
example : expand [.literal 7,.pointer 0 1] 3 [.pointer 0 2] = some [7,7] := by native_decide
example : expand [.pointer 0 1] 4 [.pointer 0 1] = none := by native_decide
example : expand [.pointer 0 1] 1 [.literal 7] = some [7] := by native_decide
example : cost 3 [.literal 7,.pointer 0 1,.pointer 0 1] = 7 := by native_decide
