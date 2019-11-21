# run as 'python -m unittest discover -s tests'

import pybombs.fetchers.git as git
import unittest

class TestUrlParsing(unittest.TestCase):

    def do_git_parse_url(self, url_in, url_expected, gitrev):
        url_out, args = git.parse_git_url(url_in,{})
        self.assertEqual(url_out,url_expected)
        self.assertEqual(args.get('gitrev'),gitrev)

#check legal git URLs with and without pybombs [@commit] suffix
#https://git-scm.com/docs/git-clone/

# test SSH variants
# ssh://[user@]host.xz[:port]/path/to/repo.git[@commit]
    def test_ssh_0000(self): self.do_git_parse_url("ssh://host.xz/path/to/pybombs.git","ssh://host.xz/path/to/pybombs.git",None)
    def test_ssh_u000(self): self.do_git_parse_url("ssh://user@host.xz/path/to/pybombs.git","ssh://user@host.xz/path/to/pybombs.git",None)
    def test_ssh_00p0(self): self.do_git_parse_url("ssh://host.xz:234/path/to/pybombs.git","ssh://host.xz:234/path/to/pybombs.git",None)
    def test_ssh_000c(self): self.do_git_parse_url("ssh://host.xz/path/to/pybombs.git@_commit-","ssh://host.xz/path/to/pybombs.git","_commit-")
    def test_ssh_u0p0(self): self.do_git_parse_url("ssh://user@host.xz:234/path/to/pybombs.git","ssh://user@host.xz:234/path/to/pybombs.git",None)
    def test_ssh_00pc(self): self.do_git_parse_url("ssh://host.xz:234/path/to/pybombs.git@_commit-","ssh://host.xz:234/path/to/pybombs.git","_commit-")
    def test_ssh_u00c(self): self.do_git_parse_url("ssh://user@host.xz/path/to/pybombs.git@_commit-","ssh://user@host.xz/path/to/pybombs.git","_commit-")
    def test_ssh_u0pc(self): self.do_git_parse_url("ssh://user@host.xz:234/path/to/pybombs.git@_commit-","ssh://user@host.xz:234/path/to/pybombs.git","_commit-")

    def test_gpssh_0000(self): self.do_git_parse_url("git+ssh://host.xz/path/to/pybombs.git","git+ssh://host.xz/path/to/pybombs.git",None)
    def test_gpssh_u000(self): self.do_git_parse_url("git+ssh://user@host.xz/path/to/pybombs.git","git+ssh://user@host.xz/path/to/pybombs.git",None) ## FAIL 4
    def test_gpssh_ut00(self): self.do_git_parse_url("git+ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","git+ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git",None) ## FAIL 5
    def test_gpssh_000c(self): self.do_git_parse_url("git+ssh://host.xz/path/to/pybombs.git@_commit-","git+ssh://host.xz/path/to/pybombs.git","_commit-")
    def test_gpssh_u00c(self): self.do_git_parse_url("git+ssh://user@host.xz/path/to/pybombs.git@_commit-","git+ssh://user@host.xz/path/to/pybombs.git","_commit-")
    def test_gpssh_ut0c(self): self.do_git_parse_url("git+ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git@_commit-","git+ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","_commit-")

    # test using tokens
    def test_ssh_ut00(self): self.do_git_parse_url("ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git",None) ##FAIL 7
    def test_ssh_utp0(self): self.do_git_parse_url("ssh://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git","ssh://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git",None)
    def test_ssh_ut0c(self): self.do_git_parse_url("ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git@_commit-","ssh://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","_commit-")
    def test_ssh_utpc(self): self.do_git_parse_url("ssh://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git@_commit-","ssh://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git","_commit-")    

# test git & ftp protocol variants
# git://host.xz[:port]/path/to/repo.git/
# ftp[s]://host.xz[:port]/path/to/repo.git/
    def test_git_0000(self): self.do_git_parse_url("git://host.xz/path/to/pybombs.git","git://host.xz/path/to/pybombs.git",None)
    def test_git_00p0(self): self.do_git_parse_url("git://host.xz:234/path/to/pybombs.git","git://host.xz:234/path/to/pybombs.git",None)
    def test_git_000c(self): self.do_git_parse_url("git://host.xz/path/to/pybombs.git@_commit-","git://host.xz/path/to/pybombs.git","_commit-")
    def test_git_00pc(self): self.do_git_parse_url("git://host.xz:234/path/to/pybombs.git@_commit-","git://host.xz:234/path/to/pybombs.git","_commit-")

    # test using tokens
    def test_git_u000(self): self.do_git_parse_url("git://user@host.xz/path/to/pybombs.git","git://user@host.xz/path/to/pybombs.git",None)
    def test_git_u0p0(self): self.do_git_parse_url("git://user@host.xz:234/path/to/pybombs.git","git://user@host.xz:234/path/to/pybombs.git",None)
    def test_git_u00c(self): self.do_git_parse_url("git://user@host.xz/path/to/pybombs.git@_commit-","git://user@host.xz/path/to/pybombs.git","_commit-")
    def test_git_u0pc(self): self.do_git_parse_url("git://user@host.xz:234/path/to/pybombs.git@_commit-","git://user@host.xz:234/path/to/pybombs.git","_commit-")
    def test_git_ut00(self): self.do_git_parse_url("git://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","git://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git",None) ##FAIL 1
    def test_git_utp0(self): self.do_git_parse_url("git://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git","git://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git",None)
    def test_git_ut0c(self): self.do_git_parse_url("git://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git@_commit-","git://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","_commit-")
    def test_git_utpc(self): self.do_git_parse_url("git://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git@_commit-","git://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git","_commit-")

# test http[s] protocol variants
# https://host.xz[:port]/path/to/repo.git/
    def test_http_0000(self): self.do_git_parse_url("https://host.xz/path/to/pybombs.git","https://host.xz/path/to/pybombs.git",None)
    def test_http_00p0(self): self.do_git_parse_url("https://host.xz:234/path/to/pybombs.git","https://host.xz:234/path/to/pybombs.git",None)
    def test_http_000c(self): self.do_git_parse_url("https://host.xz/path/to/pybombs.git@_commit-","https://host.xz/path/to/pybombs.git","_commit-")
    def test_http_00pc(self): self.do_git_parse_url("https://host.xz:234/path/to/pybombs.git@_commit-","https://host.xz:234/path/to/pybombs.git","_commit-")

    def test_gphttp_0000(self): self.do_git_parse_url("git+https://host.xz/path/to/pybombs.git","git+https://host.xz/path/to/pybombs.git",None)
    def test_gphttp_000c(self): self.do_git_parse_url("git+https://host.xz/path/to/pybombs.git@_commit-","git+https://host.xz/path/to/pybombs.git","_commit-")

    # test using tokens
    def test_http_u000(self): self.do_git_parse_url("https://user@host.xz/path/to/pybombs.git","https://user@host.xz/path/to/pybombs.git",None)
    def test_http_u0p0(self): self.do_git_parse_url("https://user@host.xz:234/path/to/pybombs.git","https://user@host.xz:234/path/to/pybombs.git",None)
    def test_http_u00c(self): self.do_git_parse_url("https://user@host.xz/path/to/pybombs.git@_commit-","https://user@host.xz/path/to/pybombs.git","_commit-")
    def test_http_u0pc(self): self.do_git_parse_url("https://user@host.xz:234/path/to/pybombs.git@_commit-","https://user@host.xz:234/path/to/pybombs.git","_commit-")
    def test_http_ut00(self): self.do_git_parse_url("https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git",None) ## FAIL 6
    def test_http_utp0(self): self.do_git_parse_url("https://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git","https://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git",None)
    def test_http_ut0c(self): self.do_git_parse_url("https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git@_commit-","https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","_commit-")
    def test_http_utpc(self): self.do_git_parse_url("https://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git@_commit-","https://user:ToKeN2-._~+/=@host.xz:234/path/to/pybombs.git","_commit-")

    def test_gphttp_u000(self): self.do_git_parse_url("git+https://user@host.xz/path/to/pybombs.git","git+https://user@host.xz/path/to/pybombs.git",None) ## FAIL 2
    def test_gphttp_ut00(self): self.do_git_parse_url("git+https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","git+https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git",None) ## FAIL 3
    def test_gphttp_u00c(self): self.do_git_parse_url("git+https://user@host.xz/path/to/pybombs.git@_commit-","git+https://user@host.xz/path/to/pybombs.git","_commit-")
    def test_gphttp_ut0c(self): self.do_git_parse_url("git+https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git@_commit-","git+https://user:ToKeN2-._~+/=@host.xz/path/to/pybombs.git","_commit-")

# test scp-like syntax
# [user@]host.xz:path/to/repo.git/
    def test_scp_0000(self): self.do_git_parse_url("host.xz:path/to/pybombs.git","host.xz:path/to/pybombs.git",None)
    def test_scp_u000(self): self.do_git_parse_url("user@host.xz:path/to/pybombs.git","user@host.xz:path/to/pybombs.git",None)
    def test_scp_000c(self): self.do_git_parse_url("host.xz:path/to/pybombs.git@_commit-","host.xz:path/to/pybombs.git","_commit-")
    def test_scp_u00c(self): self.do_git_parse_url("user@host.xz:path/to/pybombs.git@_commit-","user@host.xz:path/to/pybombs.git","_commit-")

# test local git repos
# /path/to/repo.git/
# file:///path/to/repo.git/
    def test_local_0000(self): self.do_git_parse_url("/path/to/pybombs.git","/path/to/pybombs.git",None)
    def test_local_000c(self): self.do_git_parse_url("/path/to/pybombs.git@_commit-","/path/to/pybombs.git","_commit-")
    def test_file_0000(self): self.do_git_parse_url("file:///path/to/pybombs.git","file:///path/to/pybombs.git",None)
    def test_file_000c(self): self.do_git_parse_url("file:///path/to/pybombs.git@_commit-","file:///path/to/pybombs.git","_commit-")

    def test_new_000(self): self.do_git_parse_url("git+https://user:xajwdmpmyhjbnzclrfda@githost.raleigh.signalscape.com/DTRA/wt-lora-recipes.git@tmhk-integ", "git+https://user:xajwdmpmyhjbnzclrfda@githost.raleigh.signalscape.com/DTRA/wt-lora-recipes.git", "tmhk-integ")
    def test_new_001(self): self.do_git_parse_url("git+https://user:XAjwdmpmYhJBNzcLRfdA@githost.raleigh.signalscape.com/DTRA/wt-lora-recipes.git@tmhk-integ", "git+https://user:XAjwdmpmYhJBNzcLRfdA@githost.raleigh.signalscape.com/DTRA/wt-lora-recipes.git", "tmhk-integ")
    def test_new_002(self): self.do_git_parse_url("git+https://user:fnkPdzMj6ivmrvefNzmy@githost.raleigh.signalscape.com/SS_SDR/ss_sdr-recipes.git", "git+https://user:fnkPdzMj6ivmrvefNzmy@githost.raleigh.signalscape.com/SS_SDR/ss_sdr-recipes.git", None)
    def test_new_003(self): self.do_git_parse_url("git+https://user:P5-CRN4UfDNdTURpXmGo@githost.raleigh.signalscape.com/SS_SDR/ss_sdr-patch.git", "git+https://user:P5-CRN4UfDNdTURpXmGo@githost.raleigh.signalscape.com/SS_SDR/ss_sdr-patch.git", None)
    def test_new_004(self): self.do_git_parse_url("git+https://user:HiZ_R8_ByXWevefS1NEo@githost.raleigh.signalscape.com/DTRA/wt-lora.git", "git+https://user:HiZ_R8_ByXWevefS1NEo@githost.raleigh.signalscape.com/DTRA/wt-lora.git", None)

if __name__ == '__main__':
    unittest.main()
