package(default_visibility = ["//visibility:public"])

licenses(["reciprocal"])  # Apache 2.0

## Docker rules
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
## Pip rules
load("@deps//:requirements.bzl", "requirement")

py_binary(
    name = "dnsmon",
    srcs = ["dnsmon.py"],
    deps = [ requirement("dnspython"), requirement("prometheus-client") ],
)

py3_image(
    name = "dnsmon_image",
    main = "dnsmon.py",
    srcs = ["dnsmon.py"],
    deps = [ requirement("dnspython"), requirement("prometheus-client") ],
)
