from __future__ import absolute_import, division, print_function

def cbetadev_bullseye(pdbid=""):
  return """@text
From Simon Lovell's 'CBdev_histogram_peptide.kip3'
  edited 200420 jsr

@kinemage 1 {%s CBdev bullseye}
@whitebackground
@1viewid {2D plot around Cb}
@1span 1.6457283
@1zslab 293.0
@1center -0.0972 0.0267 0
@1matrix 1 -0 0 0 1 0 0 -0 1
@2viewid {3d overview}
@2span 6.0117383
@2zslab 200.0
@2center 0 0 0
@2matrix 1 -0 0 0 1 0 0 -0 1
@group {Ala dipeptide} dominant
@subgroup {balls}
@balllist {O} color= red radius= 0.1
{ o ala 0 }1.141 -1.991 -3.085
{ o ala 1 }-0.276 2.302 -2.166
@balllist {N} color= sky radius= 0.1
{ n ala 1 }1.35 0.001 -2.059
{ n ala 2 }-2.068 0.959 -2.392
@subgroup {sidechain}
@vectorlist {meth} color= sea
{ ca ala 1 }P -0.011 0.001 -1.536
{ cb ala 1 }0 0 0
@vectorlist {methH} color= gray
{ cb ala 1 }P 0 0 0
{ hb1 ala 1 }-0.894 -0.109 0.355
{ cb ala 1 }P 0 0 0
{ hb2 ala 1 }0.496 -0.77 0.313
{ cb ala 1 }P 0 0 0
{ hb3 ala 1 }0.422 0.803 0.339
@subgroup {main ch}
@vectorlist {phiH} color= gray
{ n ala 1 }P 1.35 0.001 -2.059
{ h ala 1 }1.886 0.809 -1.815
@vectorlist {phimc} color= peachtint
{ ca ala 0 }P 3.257 -0.873 -3.276
{"}3.257 -0.873 -3.276
{ c ala 0 }1.815 -1.003 -2.795
{ o ala 0 }1.141 -1.991 -3.085
{ c ala 0 }P 1.815 -1.003 -2.795
{ n ala 1 }1.35 0.001 -2.059
{ ca ala 1 }-0.011 0.001 -1.536
@vectorlist {mcH} nobutton color= gray
{ ca ala 1 }P -0.011 0.001 -1.536
{ ha ala 1 }-0.51 -0.915 -1.884
@vectorlist {psi} color= peachtint
{ ca ala 1 }P -0.011 0.001 -1.536
{ c ala 1 }-0.802 1.194 -2.061
@vectorlist {psiH} color= gray
{ n ala 2 }P -2.068 0.959 -2.392
{ h ala 2 }-2.509 0.065 -2.312
@vectorlist {psimc} color= peachtint
{ c ala 1 }P -0.802 1.194 -2.061
{ o ala 1 }-0.276 2.302 -2.166
{ c ala 1 }P -0.802 1.194 -2.061
{ n ala 2 }-2.068 0.959 -2.392
{ ca ala 2 }-2.933 2.014 -2.907
@group {bullseye}
@subgroup {(implied)} nobutton
@vectorlist {0.125} color= green width= 1
{0.125}P 0.125 0 0
{"}0.125 0.008 0
{"}0.124 0.016 0
{"}0.123 0.023 0
{"}0.121 0.031 0
{"}0.119 0.039 0
{"}0.116 0.046 0
{"}0.113 0.053 0
{"}0.11 0.06 0
{"}0.106 0.067 0
{"}0.101 0.073 0
{"}0.096 0.08 0
{"}0.091 0.086 0
{"}0.086 0.091 0
{"}0.08 0.096 0
{"}0.073 0.101 0
{"}0.067 0.106 0
{"}0.06 0.11 0
{"}0.053 0.113 0
{"}0.046 0.116 0
{"}0.039 0.119 0
{"}0.031 0.121 0
{"}0.023 0.123 0
{"}0.016 0.124 0
{"}0.008 0.125 0
{"}-0 0.125 0
{"}-0.008 0.125 0
{"}-0.016 0.124 0
{"}-0.023 0.123 0
{"}-0.031 0.121 0
{"}-0.039 0.119 0
{"}-0.046 0.116 0
{"}-0.053 0.113 0
{"}-0.06 0.11 0
{"}-0.067 0.106 0
{"}-0.073 0.101 0
{"}-0.08 0.096 0
{"}-0.086 0.091 0
{"}-0.091 0.086 0
{"}-0.096 0.08 0
{"}-0.101 0.073 0
{"}-0.106 0.067 0
{"}-0.11 0.06 0
{"}-0.113 0.053 0
{"}-0.116 0.046 0
{"}-0.119 0.039 0
{"}-0.121 0.031 0
{"}-0.123 0.023 0
{"}-0.124 0.016 0
{"}-0.125 0.008 0
{"}-0.125 -0 0
{"}-0.125 -0.008 0
{"}-0.124 -0.016 0
{"}-0.123 -0.023 0
{"}-0.121 -0.031 0
{"}-0.119 -0.039 0
{"}-0.116 -0.046 0
{"}-0.113 -0.053 0
{"}-0.11 -0.06 0
{"}-0.106 -0.067 0
{"}-0.101 -0.073 0
{"}-0.096 -0.08 0
{"}-0.091 -0.086 0
{"}-0.086 -0.091 0
{"}-0.08 -0.096 0
{"}-0.073 -0.101 0
{"}-0.067 -0.106 0
{"}-0.06 -0.11 0
{"}-0.053 -0.113 0
{"}-0.046 -0.116 0
{"}-0.039 -0.119 0
{"}-0.031 -0.121 0
{"}-0.023 -0.123 0
{"}-0.016 -0.124 0
{"}-0.008 -0.125 0
{"}-0 -0.125 0
{"}0.008 -0.125 0
{"}0.016 -0.124 0
{"}0.023 -0.123 0
{"}0.031 -0.121 0
{"}0.039 -0.119 0
{"}0.046 -0.116 0
{"}0.053 -0.113 0
{"}0.06 -0.11 0
{"}0.067 -0.106 0
{"}0.073 -0.101 0
{"}0.08 -0.096 0
{"}0.086 -0.091 0
{"}0.091 -0.086 0
{"}0.096 -0.08 0
{"}0.101 -0.073 0
{"}0.106 -0.067 0
{"}0.11 -0.06 0
{"}0.113 -0.053 0
{"}0.116 -0.046 0
{"}0.119 -0.039 0
{"}0.121 -0.031 0
{"}0.123 -0.023 0
{"}0.124 -0.016 0
{"}0.125 -0.008 0
{"}0.125 0 0
@vectorlist {0.25} color= gold width= 3
{0.25}P 0.25 0 0
{"}0.25 0.016 0
{"}0.248 0.031 0
{"}0.246 0.047 0
{"}0.242 0.062 0
{"}0.238 0.077 0
{"}0.232 0.092 0
{"}0.226 0.106 0
{"}0.219 0.12 0
{"}0.211 0.134 0
{"}0.202 0.147 0
{"}0.193 0.159 0
{"}0.182 0.171 0
{"}0.171 0.182 0
{"}0.159 0.193 0
{"}0.147 0.202 0
{"}0.134 0.211 0
{"}0.12 0.219 0
{"}0.106 0.226 0
{"}0.092 0.232 0
{"}0.077 0.238 0
{"}0.062 0.242 0
{"}0.047 0.246 0
{"}0.031 0.248 0
{"}0.016 0.25 0
{"}-0 0.25 0
{"}-0.016 0.25 0
{"}-0.031 0.248 0
{"}-0.047 0.246 0
{"}-0.062 0.242 0
{"}-0.077 0.238 0
{"}-0.092 0.232 0
{"}-0.106 0.226 0
{"}-0.12 0.219 0
{"}-0.134 0.211 0
{"}-0.147 0.202 0
{"}-0.159 0.193 0
{"}-0.171 0.182 0
{"}-0.182 0.171 0
{"}-0.193 0.159 0
{"}-0.202 0.147 0
{"}-0.211 0.134 0
{"}-0.219 0.12 0
{"}-0.226 0.106 0
{"}-0.232 0.092 0
{"}-0.238 0.077 0
{"}-0.242 0.062 0
{"}-0.246 0.047 0
{"}-0.248 0.031 0
{"}-0.25 0.016 0
{"}-0.25 -0 0
{"}-0.25 -0.016 0
{"}-0.248 -0.031 0
{"}-0.246 -0.047 0
{"}-0.242 -0.062 0
{"}-0.238 -0.077 0
{"}-0.232 -0.092 0
{"}-0.226 -0.106 0
{"}-0.219 -0.12 0
{"}-0.211 -0.134 0
{"}-0.202 -0.147 0
{"}-0.193 -0.159 0
{"}-0.182 -0.171 0
{"}-0.171 -0.182 0
{"}-0.159 -0.193 0
{"}-0.147 -0.202 0
{"}-0.134 -0.211 0
{"}-0.12 -0.219 0
{"}-0.106 -0.226 0
{"}-0.092 -0.232 0
{"}-0.077 -0.238 0
{"}-0.062 -0.242 0
{"}-0.047 -0.246 0
{"}-0.031 -0.248 0
{"}-0.016 -0.25 0
{"}-0 -0.25 0
{"}0.016 -0.25 0
{"}0.031 -0.248 0
{"}0.047 -0.246 0
{"}0.062 -0.242 0
{"}0.077 -0.238 0
{"}0.092 -0.232 0
{"}0.106 -0.226 0
{"}0.12 -0.219 0
{"}0.134 -0.211 0
{"}0.147 -0.202 0
{"}0.159 -0.193 0
{"}0.171 -0.182 0
{"}0.182 -0.171 0
{"}0.193 -0.159 0
{"}0.202 -0.147 0
{"}0.211 -0.134 0
{"}0.219 -0.12 0
{"}0.226 -0.106 0
{"}0.232 -0.092 0
{"}0.238 -0.077 0
{"}0.242 -0.062 0
{"}0.246 -0.047 0
{"}0.248 -0.031 0
{"}0.25 -0.016 0
{"}0.25 0 0
@vectorlist {0.375} color= red width= 1
{0.375}P 0.375 0 0
{"}0.374 0.024 0
{"}0.372 0.047 0
{"}0.368 0.07 0
{"}0.363 0.093 0
{"}0.357 0.116 0
{"}0.349 0.138 0
{"}0.339 0.16 0
{"}0.329 0.181 0
{"}0.317 0.201 0
{"}0.303 0.22 0
{"}0.289 0.239 0
{"}0.273 0.257 0
{"}0.257 0.273 0
{"}0.239 0.289 0
{"}0.22 0.303 0
{"}0.201 0.317 0
{"}0.181 0.329 0
{"}0.16 0.339 0
{"}0.138 0.349 0
{"}0.116 0.357 0
{"}0.093 0.363 0
{"}0.07 0.368 0
{"}0.047 0.372 0
{"}0.024 0.374 0
{"}-0 0.375 0
{"}-0.024 0.374 0
{"}-0.047 0.372 0
{"}-0.07 0.368 0
{"}-0.093 0.363 0
{"}-0.116 0.357 0
{"}-0.138 0.349 0
{"}-0.16 0.339 0
{"}-0.181 0.329 0
{"}-0.201 0.317 0
{"}-0.22 0.303 0
{"}-0.239 0.289 0
{"}-0.257 0.273 0
{"}-0.273 0.257 0
{"}-0.289 0.239 0
{"}-0.303 0.22 0
{"}-0.317 0.201 0
{"}-0.329 0.181 0
{"}-0.339 0.16 0
{"}-0.349 0.138 0
{"}-0.357 0.116 0
{"}-0.363 0.093 0
{"}-0.368 0.07 0
{"}-0.372 0.047 0
{"}-0.374 0.024 0
{"}-0.375 -0 0
{"}-0.374 -0.024 0
{"}-0.372 -0.047 0
{"}-0.368 -0.07 0
{"}-0.363 -0.093 0
{"}-0.357 -0.116 0
{"}-0.349 -0.138 0
{"}-0.339 -0.16 0
{"}-0.329 -0.181 0
{"}-0.317 -0.201 0
{"}-0.303 -0.22 0
{"}-0.289 -0.239 0
{"}-0.273 -0.257 0
{"}-0.257 -0.273 0
{"}-0.239 -0.289 0
{"}-0.22 -0.303 0
{"}-0.201 -0.317 0
{"}-0.181 -0.329 0
{"}-0.16 -0.339 0
{"}-0.138 -0.349 0
{"}-0.116 -0.357 0
{"}-0.093 -0.363 0
{"}-0.07 -0.368 0
{"}-0.047 -0.372 0
{"}-0.024 -0.374 0
{"}-0 -0.375 0
{"}0.024 -0.374 0
{"}0.047 -0.372 0
{"}0.07 -0.368 0
{"}0.093 -0.363 0
{"}0.116 -0.357 0
{"}0.138 -0.349 0
{"}0.16 -0.339 0
{"}0.181 -0.329 0
{"}0.201 -0.317 0
{"}0.22 -0.303 0
{"}0.239 -0.289 0
{"}0.257 -0.273 0
{"}0.273 -0.257 0
{"}0.289 -0.239 0
{"}0.303 -0.22 0
{"}0.317 -0.201 0
{"}0.329 -0.181 0
{"}0.339 -0.16 0
{"}0.349 -0.138 0
{"}0.357 -0.116 0
{"}0.363 -0.093 0
{"}0.368 -0.07 0
{"}0.372 -0.047 0
{"}0.374 -0.024 0
{"}0.375 0 0
@vectorlist {0.5} color= hotpink width= 1
{0.5}P 0.5 0 0
{"}0.499 0.031 0
{"}0.496 0.063 0
{"}0.491 0.094 0
{"}0.484 0.124 0
{"}0.476 0.155 0
{"}0.465 0.184 0
{"}0.452 0.213 0
{"}0.438 0.241 0
{"}0.422 0.268 0
{"}0.405 0.294 0
{"}0.385 0.319 0
{"}0.364 0.342 0
{"}0.342 0.364 0
{"}0.319 0.385 0
{"}0.294 0.405 0
{"}0.268 0.422 0
{"}0.241 0.438 0
{"}0.213 0.452 0
{"}0.184 0.465 0
{"}0.155 0.476 0
{"}0.124 0.484 0
{"}0.094 0.491 0
{"}0.063 0.496 0
{"}0.031 0.499 0
{"}-0 0.5 0
{"}-0.031 0.499 0
{"}-0.063 0.496 0
{"}-0.094 0.491 0
{"}-0.124 0.484 0
{"}-0.155 0.476 0
{"}-0.184 0.465 0
{"}-0.213 0.452 0
{"}-0.241 0.438 0
{"}-0.268 0.422 0
{"}-0.294 0.405 0
{"}-0.319 0.385 0
{"}-0.342 0.364 0
{"}-0.364 0.342 0
{"}-0.385 0.319 0
{"}-0.405 0.294 0
{"}-0.422 0.268 0
{"}-0.438 0.241 0
{"}-0.452 0.213 0
{"}-0.465 0.184 0
{"}-0.476 0.155 0
{"}-0.484 0.124 0
{"}-0.491 0.094 0
{"}-0.496 0.063 0
{"}-0.499 0.031 0
{"}-0.5 -0 0
{"}-0.499 -0.031 0
{"}-0.496 -0.063 0
{"}-0.491 -0.094 0
{"}-0.484 -0.124 0
{"}-0.476 -0.155 0
{"}-0.465 -0.184 0
{"}-0.452 -0.213 0
{"}-0.438 -0.241 0
{"}-0.422 -0.268 0
{"}-0.405 -0.294 0
{"}-0.385 -0.319 0
{"}-0.364 -0.342 0
{"}-0.342 -0.364 0
{"}-0.319 -0.385 0
{"}-0.294 -0.405 0
{"}-0.268 -0.422 0
{"}-0.241 -0.438 0
{"}-0.213 -0.452 0
{"}-0.184 -0.465 0
{"}-0.155 -0.476 0
{"}-0.124 -0.484 0
{"}-0.094 -0.491 0
{"}-0.063 -0.496 0
{"}-0.031 -0.499 0
{"}-0 -0.5 0
{"}0.031 -0.499 0
{"}0.063 -0.496 0
{"}0.094 -0.491 0
{"}0.124 -0.484 0
{"}0.155 -0.476 0
{"}0.184 -0.465 0
{"}0.213 -0.452 0
{"}0.241 -0.438 0
{"}0.268 -0.422 0
{"}0.294 -0.405 0
{"}0.319 -0.385 0
{"}0.342 -0.364 0
{"}0.364 -0.342 0
{"}0.385 -0.319 0
{"}0.405 -0.294 0
{"}0.422 -0.268 0
{"}0.438 -0.241 0
{"}0.452 -0.213 0
{"}0.465 -0.184 0
{"}0.476 -0.155 0
{"}0.484 -0.124 0
{"}0.491 -0.094 0
{"}0.496 -0.063 0
{"}0.499 -0.031 0
{"}0.5 0 0
@group {Labels} dominant
@subgroup {Drawn objs 1} dominant
@labellist {Drawn labels} color= white
{ HB1}-0.894 -0.109 0.355
{ HB2}0.496 -0.77 0.313
{ HB3}0.422 0.803 0.339
{0.5A}-0.213 0.452 0
""" % pdbid