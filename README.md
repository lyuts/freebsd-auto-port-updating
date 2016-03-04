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
* commiting a patch.

## Solution

### Components

