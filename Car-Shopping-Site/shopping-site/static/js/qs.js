!function (e) {
    if ("object" == typeof exports && "undefined" != typeof module) module.exports = e(); else if ("function" == typeof define && define.amd) define([], e); else {
        ("undefined" != typeof window ? window : "undefined" != typeof global ? global : "undefined" != typeof self ? self : this).Qs = e()
    }
}(function () {
    return function e(r, t, o) {
        function n(a, l) {
            if (!t[a]) {
                if (!r[a]) {
                    var c = "function" == typeof require && require;
                    if (!l && c) return c(a, !0);
                    if (i) return i(a, !0);
                    var f = new Error("Cannot find module '" + a + "'");
                    throw f.code = "MODULE_NOT_FOUND", f
                }
                var s = t[a] = {exports: {}};
                r[a][0].call(s.exports, function (e) {
                    var t = r[a][1][e];
                    return n(t || e)
                }, s, s.exports, e, r, t, o)
            }
            return t[a].exports
        }

        for (var i = "function" == typeof require && require, a = 0; a < o.length; a++) n(o[a]);
        return n
    }({
        1: [function (e, r, t) {
            "use strict";
            var o = String.prototype.replace, n = /%20/g;
            r.exports = {
                default: "RFC3986", formatters: {
                    RFC1738: function (e) {
                        return o.call(e, n, "+")
                    }, RFC3986: function (e) {
                        return e
                    }
                }, RFC1738: "RFC1738", RFC3986: "RFC3986"
            }
        }, {}], 2: [function (e, r, t) {
            "use strict";
            var o = e("./stringify"), n = e("./parse"), i = e("./formats");
            r.exports = {formats: i, parse: n, stringify: o}
        }, {"./formats": 1, "./parse": 3, "./stringify": 4}], 3: [function (e, r, t) {
            "use strict";
            var o = e("./utils"), n = Object.prototype.hasOwnProperty, i = {
                allowDots: !1,
                allowPrototypes: !1,
                arrayLimit: 20,
                decoder: o.decode,
                delimiter: "&",
                depth: 5,
                parameterLimit: 1e3,
                plainObjects: !1,
                strictNullHandling: !1
            }, a = function (e, r) {
                for (var t = {}, o = r.ignoreQueryPrefix ? e.replace(/^\?/, "") : e, a = r.parameterLimit === 1 / 0 ? void 0 : r.parameterLimit, l = o.split(r.delimiter, a), c = 0; c < l.length; ++c) {
                    var f, s, u = l[c], p = u.indexOf("]="), d = -1 === p ? u.indexOf("=") : p + 1;
                    -1 === d ? (f = r.decoder(u, i.decoder), s = r.strictNullHandling ? null : "") : (f = r.decoder(u.slice(0, d), i.decoder), s = r.decoder(u.slice(d + 1), i.decoder)), n.call(t, f) ? t[f] = [].concat(t[f]).concat(s) : t[f] = s
                }
                return t
            }, l = function (e, r, t) {
                for (var o = r, n = e.length - 1; n >= 0; --n) {
                    var i, a = e[n];
                    if ("[]" === a) i = (i = []).concat(o); else {
                        i = t.plainObjects ? Object.create(null) : {};
                        var l = "[" === a.charAt(0) && "]" === a.charAt(a.length - 1) ? a.slice(1, -1) : a,
                            c = parseInt(l, 10);
                        !isNaN(c) && a !== l && String(c) === l && c >= 0 && t.parseArrays && c <= t.arrayLimit ? (i = [])[c] = o : i[l] = o
                    }
                    o = i
                }
                return o
            }, c = function (e, r, t) {
                if (e) {
                    var o = t.allowDots ? e.replace(/\.([^.[]+)/g, "[$1]") : e, i = /(\[[^[\]]*])/g,
                        a = /(\[[^[\]]*])/.exec(o), c = a ? o.slice(0, a.index) : o, f = [];
                    if (c) {
                        if (!t.plainObjects && n.call(Object.prototype, c) && !t.allowPrototypes) return;
                        f.push(c)
                    }
                    for (var s = 0; null !== (a = i.exec(o)) && s < t.depth;) {
                        if (s += 1, !t.plainObjects && n.call(Object.prototype, a[1].slice(1, -1)) && !t.allowPrototypes) return;
                        f.push(a[1])
                    }
                    return a && f.push("[" + o.slice(a.index) + "]"), l(f, r, t)
                }
            };
            r.exports = function (e, r) {
                var t = r ? o.assign({}, r) : {};
                if (null !== t.decoder && void 0 !== t.decoder && "function" != typeof t.decoder) throw new TypeError("Decoder has to be a function.");
                if (t.ignoreQueryPrefix = !0 === t.ignoreQueryPrefix, t.delimiter = "string" == typeof t.delimiter || o.isRegExp(t.delimiter) ? t.delimiter : i.delimiter, t.depth = "number" == typeof t.depth ? t.depth : i.depth, t.arrayLimit = "number" == typeof t.arrayLimit ? t.arrayLimit : i.arrayLimit, t.parseArrays = !1 !== t.parseArrays, t.decoder = "function" == typeof t.decoder ? t.decoder : i.decoder, t.allowDots = "boolean" == typeof t.allowDots ? t.allowDots : i.allowDots, t.plainObjects = "boolean" == typeof t.plainObjects ? t.plainObjects : i.plainObjects, t.allowPrototypes = "boolean" == typeof t.allowPrototypes ? t.allowPrototypes : i.allowPrototypes, t.parameterLimit = "number" == typeof t.parameterLimit ? t.parameterLimit : i.parameterLimit, t.strictNullHandling = "boolean" == typeof t.strictNullHandling ? t.strictNullHandling : i.strictNullHandling, "" === e || null === e || void 0 === e) return t.plainObjects ? Object.create(null) : {};
                for (var n = "string" == typeof e ? a(e, t) : e, l = t.plainObjects ? Object.create(null) : {}, f = Object.keys(n), s = 0; s < f.length; ++s) {
                    var u = f[s], p = c(u, n[u], t);
                    l = o.merge(l, p, t)
                }
                return o.compact(l)
            }
        }, {"./utils": 5}], 4: [function (e, r, t) {
            "use strict";
            var o = e("./utils"), n = e("./formats"), i = {
                brackets: function (e) {
                    return e + "[]"
                }, indices: function (e, r) {
                    return e + "[" + r + "]"
                }, repeat: function (e) {
                    return e
                }
            }, a = Date.prototype.toISOString, l = {
                delimiter: "&", encode: !0, encoder: o.encode, encodeValuesOnly: !1, serializeDate: function (e) {
                    return a.call(e)
                }, skipNulls: !1, strictNullHandling: !1
            }, c = function e(r, t, n, i, a, c, f, s, u, p, d, y) {
                var b = r;
                if ("function" == typeof f) b = f(t, b); else if (b instanceof Date) b = p(b); else if (null === b) {
                    if (i) return c && !y ? c(t, l.encoder) : t;
                    b = ""
                }
                if ("string" == typeof b || "number" == typeof b || "boolean" == typeof b || o.isBuffer(b)) return c ? [d(y ? t : c(t, l.encoder)) + "=" + d(c(b, l.encoder))] : [d(t) + "=" + d(String(b))];
                var m = [];
                if (void 0 === b) return m;
                var v;
                if (Array.isArray(f)) v = f; else {
                    var g = Object.keys(b);
                    v = s ? g.sort(s) : g
                }
                for (var h = 0; h < v.length; ++h) {
                    var j = v[h];
                    a && null === b[j] || (m = Array.isArray(b) ? m.concat(e(b[j], n(t, j), n, i, a, c, f, s, u, p, d, y)) : m.concat(e(b[j], t + (u ? "." + j : "[" + j + "]"), n, i, a, c, f, s, u, p, d, y)))
                }
                return m
            };
            r.exports = function (e, r) {
                var t = e, a = r ? o.assign({}, r) : {};
                if (null !== a.encoder && void 0 !== a.encoder && "function" != typeof a.encoder) throw new TypeError("Encoder has to be a function.");
                var f = void 0 === a.delimiter ? l.delimiter : a.delimiter,
                    s = "boolean" == typeof a.strictNullHandling ? a.strictNullHandling : l.strictNullHandling,
                    u = "boolean" == typeof a.skipNulls ? a.skipNulls : l.skipNulls,
                    p = "boolean" == typeof a.encode ? a.encode : l.encode,
                    d = "function" == typeof a.encoder ? a.encoder : l.encoder,
                    y = "function" == typeof a.sort ? a.sort : null, b = void 0 !== a.allowDots && a.allowDots,
                    m = "function" == typeof a.serializeDate ? a.serializeDate : l.serializeDate,
                    v = "boolean" == typeof a.encodeValuesOnly ? a.encodeValuesOnly : l.encodeValuesOnly;
                if (void 0 === a.format) a.format = n.default; else if (!Object.prototype.hasOwnProperty.call(n.formatters, a.format)) throw new TypeError("Unknown format option provided.");
                var g, h, j = n.formatters[a.format];
                "function" == typeof a.filter ? t = (h = a.filter)("", t) : Array.isArray(a.filter) && (g = h = a.filter);
                var O = [];
                if ("object" != typeof t || null === t) return "";
                var w;
                w = a.arrayFormat in i ? a.arrayFormat : "indices" in a ? a.indices ? "indices" : "repeat" : "indices";
                var A = i[w];
                g || (g = Object.keys(t)), y && g.sort(y);
                for (var x = 0; x < g.length; ++x) {
                    var N = g[x];
                    u && null === t[N] || (O = O.concat(c(t[N], N, A, s, u, p ? d : null, h, y, b, m, j, v)))
                }
                var D = O.join(f), P = !0 === a.addQueryPrefix ? "?" : "";
                return D.length > 0 ? P + D : ""
            }
        }, {"./formats": 1, "./utils": 5}], 5: [function (e, r, t) {
            "use strict";
            var o = Object.prototype.hasOwnProperty, n = function () {
                for (var e = [], r = 0; r < 256; ++r) e.push("%" + ((r < 16 ? "0" : "") + r.toString(16)).toUpperCase());
                return e
            }(), i = function (e) {
                for (var r; e.length;) {
                    var t = e.pop();
                    if (r = t.obj[t.prop], Array.isArray(r)) {
                        for (var o = [], n = 0; n < r.length; ++n) void 0 !== r[n] && o.push(r[n]);
                        t.obj[t.prop] = o
                    }
                }
                return r
            };
            t.arrayToObject = function (e, r) {
                for (var t = r && r.plainObjects ? Object.create(null) : {}, o = 0; o < e.length; ++o) void 0 !== e[o] && (t[o] = e[o]);
                return t
            }, t.merge = function (e, r, n) {
                if (!r) return e;
                if ("object" != typeof r) {
                    if (Array.isArray(e)) e.push(r); else {
                        if ("object" != typeof e) return [e, r];
                        (n.plainObjects || n.allowPrototypes || !o.call(Object.prototype, r)) && (e[r] = !0)
                    }
                    return e
                }
                if ("object" != typeof e) return [e].concat(r);
                var i = e;
                return Array.isArray(e) && !Array.isArray(r) && (i = t.arrayToObject(e, n)), Array.isArray(e) && Array.isArray(r) ? (r.forEach(function (r, i) {
                    o.call(e, i) ? e[i] && "object" == typeof e[i] ? e[i] = t.merge(e[i], r, n) : e.push(r) : e[i] = r
                }), e) : Object.keys(r).reduce(function (e, i) {
                    var a = r[i];
                    return o.call(e, i) ? e[i] = t.merge(e[i], a, n) : e[i] = a, e
                }, i)
            }, t.assign = function (e, r) {
                return Object.keys(r).reduce(function (e, t) {
                    return e[t] = r[t], e
                }, e)
            }, t.decode = function (e) {
                try {
                    return decodeURIComponent(e.replace(/\+/g, " "))
                } catch (r) {
                    return e
                }
            }, t.encode = function (e) {
                if (0 === e.length) return e;
                for (var r = "string" == typeof e ? e : String(e), t = "", o = 0; o < r.length; ++o) {
                    var i = r.charCodeAt(o);
                    45 === i || 46 === i || 95 === i || 126 === i || i >= 48 && i <= 57 || i >= 65 && i <= 90 || i >= 97 && i <= 122 ? t += r.charAt(o) : i < 128 ? t += n[i] : i < 2048 ? t += n[192 | i >> 6] + n[128 | 63 & i] : i < 55296 || i >= 57344 ? t += n[224 | i >> 12] + n[128 | i >> 6 & 63] + n[128 | 63 & i] : (o += 1, i = 65536 + ((1023 & i) << 10 | 1023 & r.charCodeAt(o)), t += n[240 | i >> 18] + n[128 | i >> 12 & 63] + n[128 | i >> 6 & 63] + n[128 | 63 & i])
                }
                return t
            }, t.compact = function (e) {
                for (var r = [{
                    obj: {o: e},
                    prop: "o"
                }], t = [], o = 0; o < r.length; ++o) for (var n = r[o], a = n.obj[n.prop], l = Object.keys(a), c = 0; c < l.length; ++c) {
                    var f = l[c], s = a[f];
                    "object" == typeof s && null !== s && -1 === t.indexOf(s) && (r.push({obj: a, prop: f}), t.push(s))
                }
                return i(r)
            }, t.isRegExp = function (e) {
                return "[object RegExp]" === Object.prototype.toString.call(e)
            }, t.isBuffer = function (e) {
                return null !== e && void 0 !== e && !!(e.constructor && e.constructor.isBuffer && e.constructor.isBuffer(e))
            }
        }, {}]
    }, {}, [2])(2)
});