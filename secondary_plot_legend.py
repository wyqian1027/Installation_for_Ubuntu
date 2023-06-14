# using ghost ax
ax2 = ax.twinx()
p1 = ax2.plot(np.NaN, np.NaN, color=colors[0], alpha=.5, ms=ms, lw=lw, ls=lss[0])
p2 = ax2.fill(np.NaN, np.NaN, color=colors[0], alpha=.2)
ax2.get_yaxis().set_visible(False)    
ax2.legend([(p1[0], p2[0])], ["Example"], loc="upper left", fontsize=legend_fs, frameon=True, handlelength=2, markerscale=1, ncol=1)
