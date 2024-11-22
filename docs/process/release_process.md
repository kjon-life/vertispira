# Release Process

## Version Numbering
We use semantic versioning with pre-1.0 notation: `0.n.m` where:
- `0` indicates pre-1.0 development phase
- `n` indicates feature releases aligned with natural cycles
- `m` indicates bug fix releases

## Release Schedule
Feature releases (`0.n.0`) align with natural cycles:
- Spring Equinox (March)
- Summer Solstice (June)
- Autumn Equinox (September)
- Winter Solstice (December)

Bug fix releases (`0.n.m`) are published as needed to address critical issues.

## Release Types

### Feature Releases (0.n.0)
Major releases containing new features and improvements. These releases may include:
- New functionality
- Major improvements
- API changes (with backward compatibility)
- Performance improvements
- New product components

### Bug Fix Releases (0.n.m)
Limited scope releases addressing:
- Security vulnerabilities
- Critical bugs affecting user workflows
- Data integrity issues
- Severe performance problems
- Blocking issues in core functionality

## Component Versioning
Our ecosystem consists of multiple components:
- `app`: Core web application
- Additional products (as released)

Each component maintains compatibility information with core `app` versions.

## Support Policy

### Active Support
- Current feature release (`0.n`)
- Previous feature release (`0.(n-1)`)
- Critical security fixes backported to supported versions

### Version Lifecycle
- Feature Support: Current release version
- Security Support: Current + previous release version
- End of Life: Two versions back

## Communication
- Release announcements posted 2 weeks before feature releases
- Breaking changes documented in release notes
- Security advisories published as needed
- Changelog maintained in repository

## Documentation
- Release notes detail all significant changes
- API documentation updated with each release
- Migration guides provided for breaking changes
- Component compatibility matrix maintained

## For Enterprise Users
Extended support options available for enterprise customers requiring longer-term version support. Please contact our team for details.

---

Note: This process may evolve as our project grows. Subscribe to our releases or watch our repository for updates.