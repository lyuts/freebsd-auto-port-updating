# Automated FreeBSD port updating infrastructure

## Introduction
FreeBSD ports collection is a package management platform which uses Makefiles (BSD Make).
It allows an easy and convenient way of installing software and takes care of port's
dependencies. A port can be treated as a set of build instructions, dependency
declarations, build configurations, package contents and integrity checks. In case
upstream doesn't support BSD out of the box, a port can have patches to be applied during
the build. Ports are maintained by maintainers who may or may not be on the FreeBSD ports
team. One of the responsibilities in maintaining a port is keeping it up to date and
functional.

## Problem
The process of updating a port consists of:
* finding out that a newer version is available.
* updating port (+ patching if needed).
* testing build of the port and its dependencies.
* preparing a patch.
* submitting a bug (aka PR/issue) to [bugzilla](https://bugs.freebsd.org/bugzilla).
* reviewing submitted patch by someone on the ports team.
* committing a patch.

Nearly all steps, except preparing and committing a patch, are time consuming and can span
over a long period of time. There are multiple reasons to that. But as a fact, by the time
a patch is committed, or ready to be committed, a newer version may be available. While
this may not be a widespread issue with stable releases of ported software, the problem is
extremely relevant for snapshot/nightly releases.

## Solution
Most of the steps in the port updating process can be automated. Which will significantly
reduce the time required to get latest version of a ported software into ports tree.
Obviously, not all port updates can be automated, and some updates will actually require
person's intervention. Minor version updates, on the other hand, in general require no
extra effort and are probably limited to just bumping the version number and updating
distinfo file. Just automating updates to minor version will significantly increase the
speed of getting newer versions (even just minor) and reduce the churn on the ports team
members. More than that, the claim is that getting minor version updates faster by
automating them is more important than any other updates. The reason for that is because
minor versions tend to have bug fixes and security updates. On a plus side, they shouldn't
introduce that many obstacles in their automation as they generally maintain backwards
compatability by keeping existing API/ABI.
Getting nightlies/snapshots faster into ports is also important for developers. For
example, you are writing software in rust and you want to ensure it builds on FreeBSD with
the latest upstream version, or, you are a user who wants to try firefox with the latest
and improved electrolysis and help test it, or you are a developer contributing to some
project. Replace rust/firefox with another project and corresponding features and you'll
get much more use cases.

### Components

### Candidates

